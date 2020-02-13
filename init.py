import os, sys

if not hasattr(sys, 'real_prefix'):
    print ("Strongly suggest you run this in a virtualenv environment")
    exit()

if sys.version[0] != "3":
    print ("Python3 pleez!")
    exit()

print ("""For each option type 'y' or 'n'

imagemagick command 'compare' is used to compare images in training test.  This is installed 
in datahub so you can skip this option unless you are installing elsewhere.""")

if input("\ninstall system requirements including imagemagick (assumes debian-based linux)?").lower()[:1] == 'y':
    os.system("sudo apt install imagemagick")

if input("\ninstall basic python requirements?").lower()[:1] == 'y':
    os.system("pip install -r requirements.txt")

if input("\ninstall gpu requirements?").lower()[:1] == 'y':
    os.system("pip install -r requirements-gpu.txt")

os.chdir("tests")
os.system("python init.py")
os.chdir("..")

if input("\ninstall training data?").lower()[:1] == 'y':
    os.system("git clone git@github.com:danx0r/beenet_data")
    os.system("pip install -e beenet_data")

if input("\ninstall models?").lower()[:1] == 'y':
    os.system("git clone --single-branch --depth=1 hub@eye0.com:/home/hub/beenet/beenet_models")
    os.system("pip install -e beenet_models")

