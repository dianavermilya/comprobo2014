import math

class PIDcontroller(object):
    def __init__(self, name="rbt"):
        self.name = name
        self._distanceFromWall = 0
        self._angleOfWallNormal = 0
        self.rotation = 0
    def setDistanceFromWall(self, distance):
    	self._distanceFromWall = distance
    def setAngleOfWallNormal(self, smallest_idx):
        self._angleOfWallNormal = smallest_idx

    def calculateRotationToFollowWall(self):
        beNormalToWall = (self._angleOfWallNormal-90)*(0.01)
        beNearWall = (self._distanceFromWall - 0.3)*(0.8)
        print self._angleOfWallNormal, self._distanceFromWall
        print beNormalToWall, beNearWall
        self.rotation = beNormalToWall + beNearWall        

    def calculateRotationToFollowObject(self, error):
        self.rotation = error*0.01

