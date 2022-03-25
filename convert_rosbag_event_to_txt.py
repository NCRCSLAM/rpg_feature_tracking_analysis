#!/usr/bin/env python
import rosbag
from tqdm import tqdm
bag = rosbag.Bag('/home/kamzero/DVS/feature_tracking_analysis_example/example/bags/simulation_3planes.bag')
with open("out.txt", 'w') as f:
    for i, (topic, msgs, t) in enumerate(bag.read_messages(topics=['/dvs/events'])):
        for single_event in tqdm(msgs.events):
            f.write(str(single_event.ts.secs +
                    single_event.ts.nsecs*1.0/1000000000)+' ')
            f.write(str(single_event.x)+' ')
            f.write(str(single_event.y)+' ')
            if(single_event.polarity == True):
                f.write("1")
            else:
                f.write("0")
            f.write('\n')
        print("Writing events between two pic, now is " + str(i)+'!')
print("Writing is over!")
