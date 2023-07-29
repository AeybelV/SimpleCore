from defines import *

# A basic register

class Register:

    def __init__(self, val=0) -> None:
        self.value = WORD(val)

    def write(self,val) -> None:
        self.value = WORD(val)

    def read(self) -> WORD:
        return self.value

# Register file for the CPU
class RegisterFile:

    def __init__(self) -> None:
        self.registers = [Register() for i in range(REGFILE_REGCOUNT)]
    
    def write(self, reg, value) -> None:
        self.registers[reg].write(value)

    def read(self, reg) -> WORD:
        return self.registers[reg].read()
    
