import os, sys

if not hasattr(sys, 'real_prefix'):
    print ("Strongly suggest you run this in a virtualenv environment")
    exit()

if sys.version[0] != "3":
    print ("Python3 pleez!")
    exit()

if input("install system requirements (assumes debian-based linux)?").lower()[:1] == 'y':
    print ("imagemagick used to compare images in training test -- not available on all systems")
    os.system("sudo apt install imagemagick")

if input("install basic python requirements?").lower()[:1] == 'y':
    os.system("pip install -r requirements.txt")

if input("install gpu requirements?").lower()[:1] == 'y':
    os.system("pip install -r requirements-gpu.txt")

if input("run balloon training test?").lower()[:1] == 'y':
    os.chdir("tests")
    os.system("python train.py")
    os.chdir("..")

if input("run pre-trained balloon detection test?").lower()[:1] == 'y':
    os.chdir("tests")
    os.system("python detect.py")
