import os, sys

if not hasattr(sys, 'real_prefix'):
    print ("Strongly suggest you run this in a virtualenv environment")
    exit()

if sys.version[0] != "3":
    print ("Python3 pleez!")
    exit()

print ("installing requirements")
os.system("pip install -r requirements.txt")
# os.system("pip install -r requirements2.txt")

if input("install tensorflow-gpu?").lower()[:1] == 'y':
    os.system("pip install -r requirements-gpu.txt")

if input("run balloon training test?").lower()[:1] == 'y':
    os.chdir("tests")
    os.system("python train.py")
    os.chdir("..")

if input("run pre-trained balloon detection test?").lower()[:1] == 'y':
    os.chdir("tests")
    os.system("python detect.py")
