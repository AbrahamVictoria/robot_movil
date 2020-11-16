#!usr/bin/env python3

import rospy
from std_msgs.msg import String

def Mensaje():
    Encendido = rospy.Publisher('Encender', String, queue = 10)
    rospy.init_node('Control', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        Msg = "Encendido correctamente"
        Encendido.publish(Msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        Mensaje()
    except rospy.ROSInterruptException:
        pass