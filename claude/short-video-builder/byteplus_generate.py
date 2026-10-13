#!/usr/bin/env python3
"""Generate one video with BytePlus Seedance 2.5 (ModelArk), end to end.

Submits a single task, polls until it finishes, downloads the mp4, and prints
token usage and calculated cost. Uses the request format verified on
2026-10-13 (task cgt-20261013225612-abj01).

Auth: if BYTEPLUS_API_KEY is set it is sent as a Bearer token; otherwise no
Authorization header is added (e.g. when a proxy injects the credential).
The key is never printed.

Never resubmits: a failed or timed-out run prints the task id, and
`--resume TASK_ID` polls/downloads that task without creating a new one.

Example:
  python3 byteplus_generate.py \
    --prompt-file prompt.txt \
    --audio-url https://example.com/hook.mp3 \
    --audio-url https://example.com/close.mp3 \
    --duration 16 --resolution 720p --out clip.mp4
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE_URL = "https://ark.ap-southeast.bytepluses.com/api/v3"
MODEL = "dreamina-seedance-2-5-260628"
DEFAULT_PRICE_PER_M_TOKENS = 10.70  # USD per million tokens (estimate, not billed amount)
TERMINAL_FAILURES = {"failed", "cancelled", "expired"}


def request(method, path, body=None):
    headers = {"Content-Type": "application/json"}
    key = os.environ.get("BYTEPLUS_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE_URL + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:1000]
        sys.exit(f"HTTP {e.code} from {method} {path}: {detail}")


def build_payload(prompt, audio_urls, duration, resolution, ratio, generate_audio, watermark):
    content = [{"type": "text", "text": prompt}]
    for url in audio_urls:
        content.append({"type": "audio_url", "audio_url": {"url": url}, "role": "reference_audio"})
    return {
        "model": MODEL,
        "content": content,
        "generate_audio": generate_audio,
        "ratio": ratio,
        "resolution": resolution,
        "duration": duration,  # integer seconds
        "watermark": watermark,
    }


def poll(task_id, interval, timeout):
    start = time.time()
    while True:
        task = request("GET", f"/contents/generations/tasks/{task_id}")
        status = task.get("status")
        elapsed = int(time.time() - start)
        print(f"[{elapsed}s] {status}", flush=True)
        if status == "succeeded":
            return task
        if status in TERMINAL_FAILURES:
            sys.exit(f"Task {task_id} ended with status {status}: {json.dumps(task.get('error'))}")
        if elapsed > timeout:
            sys.exit(f"Timed out after {timeout}s. Task {task_id} may still be running; "
                     f"re-run with --resume {task_id} (this does not create a new task).")
        time.sleep(interval)


def download(url, out_path):
    with urllib.request.urlopen(url, timeout=300) as resp, open(out_path, "wb") as f:
        while chunk := resp.read(1 << 20):
            f.write(chunk)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group()
    src.add_argument("--prompt", help="Prompt text")
    src.add_argument("--prompt-file", help="File containing the prompt text")
    p.add_argument("--audio-url", action="append", default=[],
                   help="Reference audio URL; repeat for several (referenced in the prompt as 'audio 1', 'audio 2', ...)")
    p.add_argument("--duration", type=int, default=16, help="Seconds, integer (Seedance 2.5: 4-30)")
    p.add_argument("--resolution", default="720p")
    p.add_argument("--ratio", default="9:16")
    p.add_argument("--no-generate-audio", action="store_true", help="Set generate_audio=false")
    p.add_argument("--watermark", action="store_true", help="Set watermark=true (default false)")
    p.add_argument("--out", default="output.mp4", help="Output mp4 path")
    p.add_argument("--price-per-m", type=float, default=DEFAULT_PRICE_PER_M_TOKENS,
                   help="USD per million tokens used to calculate cost")
    p.add_argument("--poll-interval", type=int, default=10)
    p.add_argument("--timeout", type=int, default=1800, help="Max seconds to wait while polling")
    p.add_argument("--resume", metavar="TASK_ID", help="Poll/download an existing task; never submits a new one")
    args = p.parse_args()

    if args.resume:
        task_id = args.resume
    else:
        prompt = args.prompt if args.prompt is not None else (
            open(args.prompt_file).read().strip() if args.prompt_file else None)
        if not prompt:
            p.error("--prompt or --prompt-file is required unless --resume is used")
        payload = build_payload(prompt, args.audio_url, args.duration, args.resolution,
                                args.ratio, not args.no_generate_audio, args.watermark)
        task_id = request("POST", "/contents/generations/tasks", payload)["id"]
        print(f"Submitted task {task_id} (resume with --resume {task_id})", flush=True)

    t0 = time.time()
    task = poll(task_id, args.poll_interval, args.timeout)
    usage = task.get("usage", {})
    tokens = usage.get("total_tokens") or usage.get("completion_tokens") or 0
    cost = tokens * args.price_per_m / 1_000_000

    video_url = task["content"]["video_url"]
    try:
        download(video_url, args.out)
        print(f"Saved {args.out} ({os.path.getsize(args.out)} bytes)")
    except Exception as e:  # keep usage/cost output even if the download host is blocked
        print(f"Download failed: {e}\nVideo URL (valid ~24h): {video_url}", file=sys.stderr)

    print(f"Task: {task_id}")
    print(f"Resolution/ratio/duration: {task.get('resolution')} {task.get('ratio')} {task.get('duration')}s")
    print(f"Tokens: {tokens}")
    print(f"Calculated cost: ${cost:.2f} (at ${args.price_per_m}/M tokens; not a billed amount)")
    print(f"Wall time this run: {int(time.time() - t0)}s")


if __name__ == "__main__":
    main()
