import subprocess
import time
commands = ["luigid","python3 manage.py runserver 0.0.0.0:8000","python3 luigi/luigi_pipeline.py uploadmodeltos3 --workers 2 --akey AKIAJX47MRD5AYURRMHA --skey 3ErYS0CYz0lJlCtRc76EIwIXHTjGH4bOlRewoVAO"]
# commands = ["luigid"]

for process in commands:
	subprocess.Popen(process.split(" "),shell=True)