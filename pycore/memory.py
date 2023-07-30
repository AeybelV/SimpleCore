from defines import *

# A Memory operation result
class MemoryResult:

    def __init__(self, status, result=WORD(0)) -> None:
        self.status:MemoryStatus = status                           # The status of the memory operation
        self.result:WORD = result                                   # If the memory operation was sucessful, contains the result of the operation if any
    
    # Returns the value of the memory operation
    def getValue(self) -> WORD:
        return self.result

# A model of memory module
class Memory:

    def __init__(self, start, size, word_size) -> None:
        
        self.mem_start = start                                      # Starting memory address
        self.word_size = word_size                                  # Word size of the memory module
        self.mem_end = start + size                                 # Ending boundary of the memory module, used for bounds checking
        self.mem_word_cnt = size // word_size                       # Number of words in the memory
        self.memory= WORD([0] * self.mem_word_cnt)                  # Zero initialized memory of words
    
    # Reads a address in memory, returns the memory access result
    def read(self, addr) -> MemoryResult:
        
        # If the read address is invalid or misaligned, return a memory error
        if(addr < self.mem_start or addr >= self.mem_end or addr % self.word_size != 0):
            return MemoryResult(MemoryStatus.MEM_ERR)
        
        # Otherwise read the value at the location
        value = self.memory[(addr-self.mem_start // self.word_size)]
        
        # Return the value and OK status code
        return MemoryResult(MemoryStatus.MEM_OK,value)
    
    # Write a value to a address in memory
    def write(self, addr, value) -> MemoryResult:

        # If the write address is invalid or misaligned, return a memory error
        if(addr < self.mem_start or addr >= self.mem_end or addr % self.word_size != 0):
            return MemoryResult(MemoryStatus.MEM_ERR)
        
        # Otherwise write to memory
        self.memory[(addr-self.mem_start // self.word_size)] = WORD(value)
        
        # Return a OK status code
        return MemoryResult(MemoryStatus.MEM_OK)


