import subprocess
import time
import sys



print(sys.argv)
commands = ["luigid","python3 manage.py runserver 0.0.0.0:8000","python3 luigi_pipeline.py uploadmodeltos3 --workers 2 --akey "+ sys.argv[0] +" --skey "+ sys.argv[0]]
# commands = ["luigid"]

subprocess.Popen(commands[0].split(" "))
subprocess.Popen(commands[1].split(" "))
subprocess.Popen(commands[2].split(" "), cwd='./luigi')