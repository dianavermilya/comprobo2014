class PIDcontroller(object):
    def __init__(self, name="rbt"):
        self.name = name
        self.distanceFromWall = None
        self.xVel = 0
    def setDistanceFromWall(self, distance):
    	self.distanceFromWall = distance
    def getDistanceFromWall(self):
        return self.distanceFromWall
    def setXVel(self):
        self.xVel = 0.1*(self.distanceFromWall - 0.2)
    def getXVel(self):
    	return self.xVel

