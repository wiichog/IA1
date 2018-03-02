class frameWork():

    def __init__(self, matrix,initial,type):
        self.matrix = matrix
        self.initial = initial
        self.type = type
        self.cost =  0

    def actions(self,s):
        x = s.x
        y = s.y
        actions = []
        try:
            if (self.matrix[x][y+1].color==(255,255,255) or self.matrix[x][y+1].color==(255,0,0)  or self.matrix[x][y+1].color==(0,255,0)):
                actions.append("abajo")
        except IndexError:
            pass
        try:
            if (self.matrix[x][y-1].color==(255,255,255) or self.matrix[x][y-1].color==(255,0,0) or self.matrix[x][y-1].color==(0,255,0)):
                if(y-1<0): pass 
                else: actions.append("arriba")
        except IndexError:
            pass
        try:
            if (self.matrix[x-1][y].color==(255,255,255) or self.matrix[x-1][y].color==(255,0,0) or self.matrix[x-1][y].color==(0,255,0)):
                if(x-1<0): pass 
                else: actions.append("izquierda")
        except IndexError:
            pass
        try:
            if (self.matrix[x+1][y].color==(255,255,255) or self.matrix[x+1][y].color==(255,0,0) or self.matrix[x+1][y].color==(0,255,0)):
                actions.append("derecha")
        except IndexError:
            pass
        return actions

    def result(self,s,a):
        x = s.x
        y = s.y
        if(a=="arriba"):
            return [self.matrix[x][y-1]]
        if(a=="abajo"):
            return [self.matrix[x][y+1]]
        if(a=="derecha"):
            return [self.matrix[x+1][y]]
        if(a=="izquierda"):
            return [self.matrix[x-1][y]]

    def goalTest(self,s):
        if(s.color==(0,255,0)): return True
        return False

    def stepCost(self,s,a,s2):
        self.cost += 1

    def pathCost(self,statesList):
        return self.cost