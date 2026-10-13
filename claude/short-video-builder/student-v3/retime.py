#!/usr/bin/env python3
"""Write cues.js from the real voice-line durations so the animation follows the voice.
usage: retime.py audio/l6.mp3 [tail_hold=1.4]   (middle lines l2-l5 keep Draft 2 timing)"""
import subprocess, sys, json
d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',sys.argv[1]]))
hold=float(sys.argv[2]) if len(sys.argv)>2 else 1.4
D=round(d+hold,2); n6=40.3
open('cues.js','w').write('window.CUES=%s;'%json.dumps({'n6':n6,'D':D,'total':round(n6+D,2)}))
print('closing speech %.2fs -> D=%.2f total=%.2f'%(d,D,n6+D))
