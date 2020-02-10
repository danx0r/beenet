import os
import balloon_test_data, base_coco_model

os.system("rm -fr ./logs party_splashed.png")

cmd = "python ../process.py train --weights %sbase_coco_model.h5 --dataset %s" % (base_coco_model.datapath(), balloon_test_data.datapath())
print (cmd)
os.system(cmd)

logs = os.listdir("./logs")
logs.sort()
weightpath = "./logs/%s/mask_rcnn_balloon_0001.h5" % logs[-1]

cmd = "python ../process.py splash --weights %s --image party.jpg" % weightpath
print (cmd)
os.system(cmd)

print ("training is stochastic so images may differ. RMSE should be under 2000, or check visually:")
cmd = "compare -metric RMSE party_splashed.png party_expected.png null:"
print (cmd)
os.system(cmd)
