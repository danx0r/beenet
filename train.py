import os
import balloon_test_data

cmd = "python balloon.py train --weights coco --dataset %s" % balloon_test_data.datapath()

print (cmd)
os.system(cmd)
