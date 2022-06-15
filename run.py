import sys
import subprocess
try:
    subprocess.call("ffmpeg")
except:
    print('error')