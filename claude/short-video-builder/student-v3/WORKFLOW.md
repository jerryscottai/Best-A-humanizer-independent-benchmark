# GPTHuman short video: saved workflow (student short, Draft 2)

Files in this folder are the working student short (1080x1920, 47.5s). To reuse: copy to /home/claude/vert2, swap content constants in index.html, re-render.

## Standing rules
- Never invent GPT Human output or scores. Real data in index.html = Washington essay run (92.82% human / 48.8 readability / 95.6% similarity, PhD tone, Balanced). Anything else must come from a real run.
- Don't claim bypassing detectors. No hand-edit step. Say "sounds like a person wrote it", never "sounds like me".
- Unbranded = no logo, no end card.
- Flag real vs mine. Say audio verified by measurement, not listening.
- Check price and tell user before paid generation. Run each paid generation once; never re-run to retry.

## Reuse decision (user, 2026-10-13)
No GPT Human API for now. Reuse the saved real Washington run. A different topic would have NO real output, so it can't be shown as real unless the user runs GPT Human and pastes the result.

## Pipeline
1. Animation: index.html, async window.__render(t). render.py (spots / full), 2 workers even/odd, DSF 0.6667 preview, 1 for 1080x1920 final. Fonts Figtree woff2 in assets/fonts (npm @fontsource/figtree). Poll frame counts; never pgrep -f.
2. Voice: ElevenLabs restricted connector, voice Jalisa 1DC6VAfJKAscIyFOOTRa, eleven_v4. creative_create_flow first, pass flow_id; generations_count 1; SAVE session_ids; signed URLs expire in 2h.
3. Presenter: fal bytedance/seedance-2.5/reference-to-video. duration is a STRING. Audio refs via signed ElevenLabs URLs (1.8-30.2s each). No face photo/video refs (content_policy_violation). Describe person in words, include flaws, "modest mouth movement". One combined continuous clip (hook, ~2s beat, closing line), then cut with silencedetect (-35dB, 0.3s). Cost ≈ $0.0214 per 1000 tokens, tokens = H*W*FPS*dur/1024 (assumed for 2.5); 16s 720p ≈ $7.40; 422 errors may be charged.
4. Network: Settings > Capabilities additional domains: storage.googleapis.com, v3b.fal.media, *.fal.media. Do not route around the proxy.
5. Audio: assemble_voice.sh -> voice_s.wav; sfx_s.py -> sfx.wav; mix_s.sh (bed volume 0.32, gentle sidechain thr 0.05 ratio 2.5 atk 80 rel 1200, alimiter 0.7, target ≈ -18 LUFS, peak < -3 dB, verify ebur128).
6. Encode: ffmpeg -framerate 30 -i frames/f%04d.jpg -i mix.wav -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -shortest out.mp4

## Not stored (binary, re-attach each new session)
- Music bed: /home/claude/build/bed604.wav (60.4s, 48k stereo, from user's music upload).
- Fonts, presenter clips (clips/combined.mp4), voice mp3s.

## Open
- Final 1080x1920 renders (student, teacher, demo) not done.
- Last-line wording: use plain "…sounds like a person wrote it".
- Presenter look consistency across videos.

## Music library (cloud)
Artifact https://claude.ai/artifact/NpibdkZ1LVXwKXSwAfC9Ln (private). Assets are audio-only .mp4 (upload takes video containers only); restore with ffmpeg -i X.mp4 -c:a copy -vn X.mp3. Fetch with Artifact action=read, path=<asset id>.
- bed-A 9b225b43de34c3b6a0d71f16e6f6f7d5, 29.0s, -12.5 LUFS
- bed-B 6810af7f02d752025323db6e3c042c87, 33.5s, -13.7 LUFS
Tracks are shorter than videos (47-58s): loop with crossfade to ~60s, then mix. Claude picks the track per video unless told.

## Final render recipe (verified on teacher short)
DSF=1 python3 render.py full ff 0 N 2 and ... 1 N 2 in parallel (N = TOTAL*30), ~1 min; ffmpeg -framerate 30 -i ff/f%04d.jpg -i <approved draft audio extracted with -c:a copy> -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a copy -shortest final.mp4
