import os

print ("installing requirements")
os.system("pip install -r requirements1.txt")
os.system("pip install -r requirements2.txt")

if input("install tensorflow-gpu?").lower()[:1] == 'y':
    os.system("pip install -r tensorflow_gpu.txt")

if input("install available trained model: openfootballoon (245 Mbyte)?").lower()[:1] == 'y':
    os.system("pip install -r models.txt")

if input("install available datasets via_annotated_1 & test_balloons (60 Mbyte)?").lower()[:1] == 'y':
    os.system("pip install -r datasets.txt")

if input("run training (break out with ctl-C)?").lower()[:1] == 'y':
    os.chdir("samples/balloon")
    os.system("python train.py")

if input("run pre-trained splash test?").lower()[:1] == 'y':
    os.chdir("samples/balloon")
    os.system("python detect.py")
