# import Module_Packages
# from Module_Packages import *
from Module_Packages import show, display
# from Module_Packages import show as s
import sys
import __init__
# from CustomStringFunc import cust_len
import CustomStringFunc
# import Testing_init_      # Cannot import due to absence of __init__.py
# from .Module_Packages import display   # Import from current directory
# from ..ParentModule import show     # Import from parent directory
# from ...CustomStringFunc import  cust_min  # Import from parent-parent (grandparent) directory

show()

def display():
    print("Hello myprg display")

if __name__ == "__main__":
    display()

for p in sys.path:       # Search on which all paths?
    print(p)
# print(sys.path)

print()

__init__.myinit()

# You can use it to:
#               i) Initialize variables
#              ii) Import submodules for easier access
# Set up logging
# Perform configuration


# Without it (in Python < 3.3), you couldn’t import modules from that directory.
print(CustomStringFunc.cust_len("Hello"))