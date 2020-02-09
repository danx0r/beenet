import os
import balloon_test_model

cmd = "python3 balloon.py splash --weights %smask_rcnn_balloon_ep1.h5 --image party.jpg" % balloon_test_model.datapath()

print (cmd)
os.system(cmd)

cmd = "diff -s party_splashed.png party_expected.png"

print ("TEST PASSES UNLESS diff fails:")
print (cmd)
os.system(cmd)
