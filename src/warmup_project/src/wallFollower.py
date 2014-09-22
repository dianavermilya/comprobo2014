import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from PID_controller import PIDcontroller
import math


class WallFollower(object):
    def __init__(self):
        self.pid = PIDcontroller("Ribbit")


    def runController(self):
        print "run Controller"
        count = 0
        pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
        rospy.Subscriber("scan", LaserScan, self.detect)
        rospy.init_node('controller', anonymous=True)
        r = rospy.Rate(10) #hz
        message = Twist()
        while not rospy.is_shutdown():
            rotation = self.pid.rotation
            message.angular.z = rotation
            message.linear.x = 0.1
            pub.publish(message)
    
    def detect(self, data):
        arr = data.ranges
        avgs = []

        for i in range(360):
            count = 0
            total = 0
            for j in range(-2, 3):
                val = arr[(i+j)%360]
                if val != 0.0:
                    total += val
                    count += 1
            if count == 0:
                avg = 1000000.0
            else:
                avg = total/count
            avgs.append(avg)
        if not self.detectObject(avgs):
            self.detectWall(avgs)
    
    def detectObject(self, avgs):
        first = None
        angle_seg = None
        for i in range(len(avgs)):
            if avgs[i] < 0.5 and first == None:
                    first = i
            elif avgs[i] > 0.5 and first != None:
                angle_seg = [first, i]
                first = None

        if angle_seg == None:
            return False
            
        if angle_seg[0] == 0 and first != None:
            angle_seg[0] = first - 360
     
        if angle_seg[1] - angle_seg[0] < 45:
            index_range = (angle_seg[1] - angle_seg[0] + 360) % 360
            central_index = (int(math.floor(index_range/2.0)) + angle_seg[0]) % 360
            if central_index > 180:
                error = 360 - central_index
            else:
                error = central_index
            self.pid.calculateRotationToFollowObject(error)
            print "follow object", error
            return True
        return False



    def detectWall(self, avgs):
        smallest = min(avgs)
        smallest_idx = avgs.index(smallest)
        self.pid.setDistanceFromWall(smallest)
        self.pid.setAngleOfWallNormal(smallest_idx)
        self.pid.calculateRotationToFollowWall()
        #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)

    



if __name__ == "__main__":
    try:
        follower = WallFollower()
        follower.runController()
    except rospy.ROSInterruptException: pass