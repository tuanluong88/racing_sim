#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist

def talker():
    pub1 = rospy.Publisher('/ackermann_steering_controller/cmd_vel', Twist, queue_size=1)
    pub2 = rospy.Publisher('/rb2/ackermann_steering_controller/cmd_vel', Twist, queue_size=1)

    # Create a Twist message and add linear x and angular z values
    move_cmd_rb1 = Twist()
    move_cmd_rb1.linear.x = 2.0
    move_cmd_rb1.linear.y = 0.1
    move_cmd_rb1.linear.z = 0

    move_cmd_rb1.angular.x = 0
    move_cmd_rb1.angular.y = 0
    move_cmd_rb1.angular.z = 0

    move_cmd_rb2 = Twist()
    move_cmd_rb2.linear.x = 2.0
    move_cmd_rb2.angular.z = 0

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        rospy.loginfo(move_cmd_rb1)
        rospy.loginfo(move_cmd_rb2)

        pub1.publish(move_cmd_rb1)
        pub2.publish(move_cmd_rb2)
        rate.sleep()
    pub2.publish(move_cmd_rb1)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
