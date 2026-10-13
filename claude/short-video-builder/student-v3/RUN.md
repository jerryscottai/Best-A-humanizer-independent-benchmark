# Student short v3: run order (everything in this folder; no Project access needed)
Audio: voice lines l1-l6 + bed A are in the music library artifact https://claude.ai/artifact/NpibdkZ1LVXwKXSwAfC9Ln (Artifact action=read, path=<id>); audio-only mp4 -> `ffmpeg -i X.mp4 -c:a copy -vn X.mp3`.
 l1 84c8c09e9ac4a4bffce11de3492c8ce0 | l2 24d69fe215aabe6a3fb7d5c60ab0a006 | l3 bda3bf5e4984ea2182c0e9a7e0e30d62 | l4 c3d92dea4153fddde74e0669de65592f | l5 9feb75590f825eb6454e2741eba2f7aa | l6 (new closer, 3.55s) c9bd41b739bb87ed9e98fa620d7b6a97 | bed A 9b225b43de34c3b6a0d71f16e6f6f7d5
Public audio URLs for BytePlus: audio 1 https://v3b.fal.media/files/b/0aae3a2a/XBszezEwn2okWSLQYRoVt_student_l1_hook.mp3 ; audio 2 https://v3b.fal.media/files/b/0aae3b51/oQiJWV8CiQhtlb4LnIZ-5_student_v3_l6_close.mp3
1. python3 ../byteplus_generate.py --prompt-file prompt.txt --audio-url <audio1> --audio-url <audio2> --duration 16 --resolution 720p --ratio 9:16 --out clips/combined.mp4   (ONCE, ~$3.71, approved by user)
2. python3 retime.py audio/l6.mp3  -> cues.js (total 45.25s). Cut clip: hook part = first 6.5s (p1 frames @24fps), closing = 8.7s onward (p6 frames) via silencedetect -35dB 0.3s.
3. assemble_voice.sh, sfx_s.py, mix_s.sh are still set to 47.5s: change to total 45.25, closing at 40.3, bed fade ~43.2.
4. DSF=1 render.py full ... then encode (see WORKFLOW.md). Fonts: npm @fontsource/figtree -> assets/fonts.
Rules: never invent GPT Human output/scores (Washington run is real); plain closing line; unbranded; measure loudness, don't claim listening.
