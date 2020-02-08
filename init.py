import os, sys

if not hasattr(sys, 'real_prefix'):
    print ("Strongly suggest you run this in a virtualenv environment")
    exit()

if sys.version[0] != "3":
    print ("Python3 pleez!")
    exit()

print ("installing requirements")
os.system("pip install -r requirements.txt")

if input("install tensorflow-gpu?").lower()[:1] == 'y':
    os.system("pip install -r tensorflow_gpu.txt")

if input("install training data in user mode?").lower()[:1] == 'y':
    os.system("pip install git+https://github.com/danx0r/beenet_data")

elif input("install training data in developer mode?").lower()[:1] == 'y':
    os.system("git clone git@github.com:danx0r/beenet_data")
    os.system("pip install -e beenet_data")

if input("install models in user mode?").lower()[:1] == 'y':
    os.system("pip install git+ssh://hub@eye0.com:/home/hub/beenet/beenet_models#egg=beenet_coco_model")

elif input("install models in developer mode?").lower()[:1] == 'y':
    os.system("git clone git+ssh://hub@eye0.com:/home/hub/beenet/beenet_models#egg=beenet_coco_model")
    os.system("pip install -e beenet_models")
