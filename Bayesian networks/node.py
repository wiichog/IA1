import itertools

class node(object):
    
    def __init__(self, name,independent):
        self.name = name
        self.independent = independent
        self.transitions = []
        self.negativeEquations = []
        self.positiveEquations = []
        self.numberOfEquations = 0
    
    def setNumberOfEquations(self):
        self.numberOfEquations +=1
    
    def setTransitions(self,transition):
        self.setNumberOfEquations()
        self.transitions.append(transition)

    def getTransitions(self):
        return self.transitions
    
    def getIndependet(self):
        return self.independent
    
    def getNumberOfEquations(self):
        return (2**self.numberOfEquations)
    
    def setEquations(self):
        if(self.independent):
            self.positiveEquations.append(self.name)
            self.negativeEquations.append("!"+self.name)
        else:
            dependencies = [ transition.split(":")[0] for transition in self.transitions]
            table = list(itertools.product([False, True], repeat=len(dependencies)))
            for ecuation in table:
                positiveEcuation = self.name+"|"
                negativeEcuation = "!"+self.name+"|"
                for i in range(0,len(ecuation)):
                    if(ecuation[i]):
                        positiveEcuation+= dependencies[i]+","
                        negativeEcuation+= dependencies[i]+","
                    else:
                        positiveEcuation+= "!"+dependencies[i]+","
                        negativeEcuation+= "!"+dependencies[i]+","
                self.positiveEquations.append(positiveEcuation[:-1])
                self.negativeEquations.append(negativeEcuation[:-1])

    def getEquations(self,NP):
        if(NP==1): return self.positiveEquations
        else: return self.negativeEquations