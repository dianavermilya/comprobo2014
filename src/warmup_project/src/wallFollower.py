import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from PID_controller import PIDcontroller


class WallFollower(object):
    def __init__(self):
        self.pid = PIDcontroller("Ribbit")
        self.distanceFromWall = None
        self.xVel = 0


    def runController(self):
        count = 0
        pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
        rospy.Subscriber("scan", LaserScan, self.callback)
        rospy.init_node('controller', anonymous=True)
        r = rospy.Rate(10) #hz
        message = Twist()
        while not rospy.is_shutdown():
            count = self.detectWall(count)
            message.linear.x = self.pid.getXVel()
            pub.publish(message)


    def callback(self, data):
        r = data.ranges
        avg =(r[358] + r[359] + r[0] + r[1] + r[2])/5
        self.pid.setDistanceFromWall(avg)
        self.pid.setXVel()
        print avg

        #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
        self.pid.setDistanceFromWall(2.10)
        print len(data.ranges)

    def detectWall(self, count):
        #rospy.init_node('listener', anonymous=True)
        count = count + 1
        return count
    



if __name__ == "__main__":
    try:
        follower = WallFollower()
        follower.runController()
    except rospy.ROSInterruptException: pass