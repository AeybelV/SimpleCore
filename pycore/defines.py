import numpy as np
from enum import Enum

# CPU Wide Definitions

WORD                        =np.uint32

# CPU Configuration

REGFILE_REGCOUNT            =32

# Memory Result

class MemoryStatus(Enum):
    MEM_OK                  =0
    MEM_ERR                 =1

# Python SimpleCore Program Error Codes

PYSC_OK                     =0
PYSC_ERR_PROGRAM_NAME       =1

# CPU Exceptions

class RISCVException(Enum):
    RV_EXC_OK               =0
    RV_EXC_ILLEGAL_INST     =1
    RV_EXC_ERROR            =2
