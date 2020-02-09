import os
import open_footwear_images

cmd = """
python balloon.py train --weights coco --dataset %stest_balloons/balloon/
""" % open_footwear_images.datapath

print (cmd)
os.system(cmd)
