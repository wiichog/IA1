class node(object):
    color = ()
    visited = False
    x = 0
    y = 0

    def __init__(self,color,visited,initial):
        self.color = color
        self.visited = visited
        self.initial = initial

    def setPosition(self,x,y):
        self.x = x
        self.y = y
