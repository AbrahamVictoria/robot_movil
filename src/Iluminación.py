#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def Mensaje(data):
    print(data.data)

def Iluminacion():
    rospy.Subscriber("Encender", String, Mensaje)
    rospy.init_node("Luz", anonymous = True)
    rospy.spin()

if __name__ == '__main__':
    Iluminacion()