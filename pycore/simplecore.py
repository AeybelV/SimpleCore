import sys
from defines import *
from program import *
from memory import *
from cpu import *

# Debug flag, prints a debug log/trace and keeps track of stats.
DEBUG = True

def main():

    # Checks if a RISCV executable is passed as a CLI argument 
    if(len(sys.argv) < 2):
        print("No RISC-V Program Provided",file=sys.stderr)
        sys.exit(PYSC_ERR_PROGRAM_NAME)

    program_filepath = sys.argv[1]

    # The TVM to be tested
    imem: Memory = Memory(0,0,32)                                   # Instruction Memory, currently instantiated with dummy parameter
    dmem: Memory = Memory(0,0,32)                                   # Data Memory, currently instantiated with dummy parameters
    program_entry = Program.load(program_filepath)                  # ELF Loader. A pseudo "bootloader" that loads the ELF executable
                                                                    # TODO: Prototype should be changed to load into imem and dmem 
    cpu: CPU = CPU(program_entry,imem, dmem, debug=DEBUG)           # Instantiates the CPU, optional debug flag to print debug messages
    
    # CPU Loop
    while True:

        status: RISCVException = cpu.single_step()

        if(status != RISCVException.RV_EXC_OK):                     # If the CPU triggered a exception, print to stderr and exit
            print("Encountered a CPU Exception", file=sys.stderr)
            sys.exit(-1)                                            # TODO: Replace with better error code

if __name__ == "__main__":
    main()
