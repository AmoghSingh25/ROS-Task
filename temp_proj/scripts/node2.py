#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32, Float32
import rosbag


def write_data(temp):
    bag = rosbag.Bag('node2.bag', 'w')
    try:
        i = Float32()
        i.data = temp
        bag.write('temperature', i)
    finally:
        bag.close()

def pubCelsius(temp):
    C = (temp.data - 32) * 5.0/9.0
    pub = rospy.Publisher('/celsius', Float32, queue_size=10)
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(1)
    write_data(C)
    pub.publish(C)
    rate.sleep()
    
def listener():
    rospy.init_node('node2', anonymous=True)
    rospy.Subscriber("/fahrenheit", Int32, pubCelsius)
    rospy.spin()

if __name__ == '__main__':
    listener()