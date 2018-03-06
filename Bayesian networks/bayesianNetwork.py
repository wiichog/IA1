import node 
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
            itertools.chain(*[self.nodes.get(k).setEquations() for k in self.nodes.keys()])
            print("Se cumplio el numero de reglas dadas")
            duplicates = self.completelyDescribed(leftSide,1)
            duplicates = self.completelyDescribed(duplicates,2) 
            if(len(duplicates)==0):
                print("La red esta completamente descrita")
                print("La distribucion conjunta de la red es: ",self.compact())
            else:
                print("La red no esta completamente descrita")
        else:
            print("se necesitan de mas reglas")
        

    def completelyDescribed(self,leftSide,number):
        self.equations.extend(list(set(itertools.chain(*[self.nodes.get(k).getEquations(number) for k in self.nodes.keys()]))))
        duplicates = list(set(self.equations)&set(leftSide))
        [leftSide.remove(equation) for equation in duplicates]
        return leftSide
    
    def compact(self):
        compact = ""
        for key in self.nodes.keys():
            node = self.nodes.get(key)
            if(node.independent):
                compact += "P("+node.name+")"
            else:
                compact += "P("+node.name+"|"+''.join([""+transition.split(":")[0]+"," for transition in node.transitions])[:-1]+")"
        return compact
    
    def factors(self,description):
        leftSide = [line.split("=")[0].lower().replace(" ", "").replace("p","").replace("(","").replace(")","").upper() for line in description]
        rightSide = [line.split("=")[1].lower().replace(" ", "").replace("p","").replace("(","").replace(")","").upper() for line in description]
        print("Factores de la red Bayesiana")
        for key in self.nodes.keys():
            print("Factores de "+self.nodes.get(key).name+"")
            for equation in self.nodes.get(key).positiveEquations:
                try:
                    index = leftSide.index(equation)
                    print(equation +"="+ rightSide[index])
                except Exception as e:
                    print("1"+equation +"="+ str(1-float(rightSide[index])))
            for equation in self.nodes.get(key).negativeEquations:
                try:
                    index = leftSide.index(equation)
                    print(equation +"="+ rightSide[index])
                except Exception as e:
                    index = leftSide.index(equation[1:])
                    print("2"+equation +"="+ str(1-float(rightSide[index])))