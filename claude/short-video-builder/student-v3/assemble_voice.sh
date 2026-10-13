#!/bin/bash
# Voice track for the student short (47.5s): presenter clips' own audio (A: 0-6.5s, B: 8.7-15.9s of combined.mp4)
# + Jalisa lines L2-L5 from audio/l2..l5.mp3. Each source loudnorm'd to -17 LUFS, then mixed at fixed times.
cd /home/claude/vert2
ffmpeg -y -loglevel error \
 -ss 0 -t 6.5 -i clips/combined.mp4 -ss 8.7 -t 7.2 -i clips/combined.mp4 \
 -i audio/l2.mp3 -i audio/l3.mp3 -i audio/l4.mp3 -i audio/l5.mp3 \
 -filter_complex "
 [0:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,afade=t=out:st=6.3:d=0.2,adelay=0|0[a0];
 [1:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,afade=t=in:d=0.05,adelay=40300|40300[a1];
 [2:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,adelay=6900|6900[a2];
 [3:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,adelay=15400|15400[a3];
 [4:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,adelay=21900|21900[a4];
 [5:a]aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-17:TP=-3,adelay=30400|30400[a5];
 [a0][a1][a2][a3][a4][a5]amix=inputs=6:normalize=0:duration=longest,apad=whole_dur=47.5,atrim=0:47.5[o]" \
 -map "[o]" -ac 2 -ar 48000 voice_s.wav
