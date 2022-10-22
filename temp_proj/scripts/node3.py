#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32, Float32
import rosbag

def write_data(temp):
    bag = rosbag.Bag('node3.bag', 'w')
    try:
        i = Float32()
        i.data = temp
        bag.write('temperature', i)
    finally:
        bag.close()

def callback(data):
    rospy.loginfo(data.data)
    write_data(data.data)
    
def listener():
    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("/celsius", Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()