from defines import *

# A Register Component
class Register:

    def __init__(self, val=0) -> None:
        self.value: WORD = WORD(val)
    
    # Writes a value to the register
    def write(self,val) -> None:
        self.value = WORD(val)
    
    # Reads the value in the register
    def read(self) -> WORD:
        return self.value

# Register file for the CPU
class RegisterFile:

    def __init__(self) -> None:
        self.registers = [Register() for i in range(REGFILE_REGCOUNT)]
    
    # Write the value to the specified register
    def write(self, reg, value) -> None:
        # Writing to zero register does nothing
        if(reg != 0):
            self.registers[reg].write(value)
    
    # Reads the value in the specified register
    def read(self, reg) -> WORD:
        return self.registers[reg].read()
    
