import os.path
from os import path

for i in range(25):
    file = "Day%s.py" % (i+1)
    if path.exists(file):
        print("-------------------")
        print("|      Day %s      |" % (i+1))
        print("-------------------")
        exec(open(file).read())