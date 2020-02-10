import os
import balloon_test_data, base_coco_model

if input("delete logs?").lower()[:1] == 'y':
    os.system("rm -fr ./logs")

cmd = "python balloon.py train --weights %sbase_coco_model.h5 --dataset %s" % (base_coco_model.datapath(), balloon_test_data.datapath())
print (cmd)
os.system(cmd)

logs = os.listdir("./logs")
logs.sort()
weightpath = "./logs/%s/mask_rcnn_balloon_0001.h5" % logs[-1]

cmd = "python3 balloon.py splash --weights %s --image party.jpg" % weightpath
print (cmd)
# os.system(cmd)

print ("training is stochastic so images may differ. RMSE should be under 2000, or check visually:")
cmd = "compare -metric PSNR party_splashed.png party_expected.png null:"
print (cmd)
os.system(cmd)
