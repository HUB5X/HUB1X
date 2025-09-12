import os
import sys
import subprocess

os.system('git pull --quiet')
subprocess.run([sys.executable, "script/__init__.py"])