#!/usr/bin/env python
import rospy
import rosbag
from std_msgs.msg import String, Int32
import random



def write_data(temp):
    bag = rosbag.Bag('node1.bag', 'w')
    try:
        i = Int32()
        i.data = temp
        bag.write('temperature', i)
    finally:
        bag.close()


def getTemp():
    return random.randint(0,100)

def talker():
    pub = rospy.Publisher('/fahrenheit', Int32, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        temp = getTemp()
        pub.publish(temp)
        write_data(temp)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
