import numpy as np
import rospy
from geometry_msgs.msg import Twist

class KeyboardControl:
    def __init__(self):
        rospy.init_node('Script_controlling_ARDrone', anonymous=False)
        self.pub = rospy.Publisher('/ackermann_steering_control/cmd_vel', Twist, queue_size=1, latch=True)
        self.rate = rospy.Rate(10) #10Hz


def main():
    try:
        kc = KeyboardControl()
        twist = Twist()
        twist.linear.x = 2
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        while not rospy.is_shutdown():
            #Do any needed edits to the twist message here
            kc.pub.publish(twist)
            kc.rate.sleep()
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down")

if __name__ == '__main__':
    main()