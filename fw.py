from abc import ABC, abstractmethod

class frameWork(ABC):
 
    def __init__(self, matrix):
        self.matrix = matrix
    
    @abstractmethod
    def actions(self,s):
        pass

    @abstractmethod
    def result(self,s,a):
        pass

    @abstractmethod
    def goalTest(self,s):
        pass

    @abstractmethod
    def stepCost(self,s,a,s2):
        pass

    @abstractmethod
    def pathCost(self,statesList):
        pass