from defines import *
from register import *
from alu import *
from decoder import *
from memory import *

import sys

class CPU:

    def __init__(self, entrypoint, imem, dmem, debug=False) -> None:
        
        # Instantiates CPU components
        self.pc: Register = Register(entrypoint)
        self.registers: RegisterFile = RegisterFile()
        self.alu: ALU = ALU()
        self.imem: Memory = imem
        self.dmem: Memory = dmem
        self.decoder: Decoder = Decoder()
        
        # 
        self._debug: bool = debug
    
    # Single steps the CPU. Returns a status as to whether the cpu step was succesful
    def single_step(self) -> RISCVException:
        
        # ==================================================
        #               Instruction Fetch
        # ==================================================
        
        # Memory operation to fetch the next instruction
        instruction_fetch = self.imem.read(self.pc.read())
        
        # Checks if the instruction memory read was succesful
        if(instruction_fetch.status != MemoryStatus.MEM_OK):
            print("Encountered a Memory Error in Instruction Fetch", 
                  file=sys.stderr)
            return RISCVException.RV_EXC_ERROR                      # TODO: Maybe replace with better exception code? 
        
        # Extracts the instruction
        instruction = instruction_fetch.getValue()


        # ==================================================
        #               Instruction Decode
        # ==================================================

        pass

        # ==================================================
        #               Instruction Execution
        # ==================================================

        pass
        
        
        # ==================================================
        #                   Memory Access
        # ==================================================

        pass


        # ==================================================
        #                     Writeback
        # ==================================================
        
        pass

        return RISCVException.RV_EXC_OK


