#!/bin/bash
# Final audio mix: music bed (ducked under voice) + voice + sfx. Usage: mix_s.sh <voice.wav> <out.wav>
cd /home/claude/vert2
ffmpeg -hide_banner -loglevel error -y -i /home/claude/build/bed604.wav -i "$1" -i sfx.wav -filter_complex "[0:a]atrim=0:47.5,volume=0.32,afade=t=in:d=0.8,afade=t=out:st=45.5:d=2[bed];[1:a]asplit[v1][v2];[bed][v2]sidechaincompress=threshold=0.05:ratio=2.5:attack=80:release=1200[duck];[duck][v1][2:a]amix=inputs=3:normalize=0:duration=longest,volume=-2.3dB,alimiter=limit=0.7[o]" -map "[o]" "$2"
ffmpeg -i "$2" -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2
