#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import TextMessage

def talker():
    pub = rospy.Publisher('chatter', TextMessage, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_world_message = TextMessage()
        hello_world_message.text_message = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_world_message)
        pub.publish(hello_world_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

