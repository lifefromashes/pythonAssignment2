# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# yourdict = mydict
# yourdict["elephant"] = 999
# print(mydict["elephant"])

class Point:

    def __init__(self, initX, initY):

        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) // 2
        my = (self.y + target.y) // 2
        return Point(mx, my)

p = Point(6, 4)
q = Point(8, 12)
mid = p.halfway(q)

print(mid)
