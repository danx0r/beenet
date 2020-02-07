import os

print ("installing requirements")
os.system("pip install -r requirements.txt")

if input("install tensorflow-gpu?").lower()[:1] == 'y':
    os.system("pip install -r tensorflow_gpu.txt")

if input("install beenet_data in developer mode?").lower()[:1] == 'y':
    os.system("git clone git@github.com:danx0r/beenet_data")
    os.system("pip install beenet_data")

if input("install beenet_data in udser mode?").lower()[:1] == 'y':
    os.system("pip install git+https://github.com/danx0r/beenet_data")
