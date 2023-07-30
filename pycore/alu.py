from defines import *

class ALU:
    def __init__(self) -> None:
        pass

    def ADD(self, a,b) -> WORD:
        return a+b
    
    def SUB(self, a,b) -> WORD:
        return a-b
    
    def AND(self, a,b) -> WORD:
        return a & b
    
    def OR(self,a,b) -> WORD:
        return a | b
    
    def XOR(self,a,b) -> WORD:
        return a ^ b
    
    # TODO: Add the remaining operations
    
