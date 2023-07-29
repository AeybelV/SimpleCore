from defines import *

class MemoryResult:

    def __init__(self, status, result=WORD(0)) -> None:
        
        self.status = status
        self.result = result

    def getValue(self) -> WORD:
        
        return self.result

class Memory:

    def __init__(self, start, size, word_size) -> None:
        
        self.mem_start = start
        self.word_size = word_size
        self.mem_end = start + size
        self.mem_word_cnt = size // word_size
        self.memory= WORD([0] * self.mem_word_cnt)

    def read(self, addr) -> MemoryResult:

        if(addr < self.mem_start or addr >= self.mem_end or addr % self.word_size != 0):
            return MemoryResult(MEM_ERR)
        
        value = self.memory[(addr-self.mem_start // self.word_size)]

        return MemoryResult(MEM_OK,value)
    
    def write(self, addr, value) -> MemoryResult:

        if(addr < self.mem_start or addr >= self.mem_end or addr % self.word_size != 0):
            return MemoryResult(MEM_ERR)

        self.memory[(addr-self.mem_start // self.word_size)] = WORD(value)

        return MemoryResult(MEM_OK)


