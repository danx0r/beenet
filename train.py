import os
import balloon_test_data, base_coco_model

cmd = "python balloon.py train --weights %sbase_coco_model.h5 --dataset %s" % (base_coco_model.datapath(), balloon_test_data.datapath())

print (cmd)
#os.system(cmd)
