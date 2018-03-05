import node 
import transition
import itertools

class bayesianNetwork():

    nodes = {}
    numberOfRules = 0
    equations = []

    def __init__(self,description):
        leftSide = [line.split("=")[0].lower().replace(" ", "").replace("p","").replace("(","").replace(")","").upper() for line in description]
        rightSide = [line.split("=")[1].lower().replace(" ", "").replace("p","").replace("(","").replace(")","").upper() for line in description]
        self.numberOfRules = len(leftSide)
        transitions = []
        for i in range(0,len(leftSide)):
            if(leftSide[i].find("|")==-1 and leftSide[i].find(",")==-1):
                name = leftSide[i]
                self.nodes[name] = node.node(name,True)
            else:
                name = leftSide[i].split("|")
                leftVariable = name[0].replace("!","")
                self.nodes[leftVariable] = node.node(leftVariable,False)
                rightVariable = name[1].replace("!","").split(",")
                transitions.extend([(variable+":"+leftVariable) for variable in rightVariable if (variable+":"+leftVariable) not in transitions])
        for tran in transitions:
            toNode = tran.split(":")[1]
            self.nodes.get(toNode).setTransitions(tran)
        number = sum([self.nodes.get(k).getNumberOfEquations() for k in self.nodes.keys()])
        if(number==self.numberOfRules):
            print("Se cumplio el numero de reglas dadas")
        else:
            print("se necesitan de mas reglas")
        duplicates = self.completelyDescribed(leftSide,1)
        duplicates = self.completelyDescribed(duplicates,2)   
        if(len(duplicates)==0):
            print("La red esta completamente descrita")
        else:
            print("La red no esta completamente descrita")

    def completelyDescribed(self,leftSide,number):
        self.equations = list(itertools.chain(*[self.nodes.get(k).setEquations(number) for k in self.nodes.keys()]))
        duplicates = list(set(self.equations)&set(leftSide))
        [leftSide.remove(equation) for equation in duplicates]
        return leftSide