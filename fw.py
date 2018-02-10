from abc import ABC, abstractmethod

class AbstractOperation(ABC):
 
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()
    
    @abstractmethod
    def execute(self):
        pass