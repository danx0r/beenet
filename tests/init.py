import os

if input("\ninstall pre-trained detection test  model and run test?").lower()[:1] == 'y':
    os.system("pip install --index http://hub.datahub.host/ --trusted-host hub.datahub.host -r requirements-detect.txt")
    os.system("python detect.py")

if input("\ninstall test data & base coco model, and run training test (< 5 minutes with gpu, > 1 hr without)?").lower()[:1] == 'y':
    os.system("pip install --index http://hub.datahub.host/ --trusted-host hub.datahub.host -r requirements-train.txt")
    os.system("python train.py")

