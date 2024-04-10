This repository purpose is to add the package folder into the system path so the system know where to look for this package's modules.

# import Path class of "pathlib" module
from pathlib import Path

# import "system" module
import sys
# _______________________IMPORTANT________________________
# create a Path object name "path_root"
# "__file__" is a special variable contains the path of the current script
# .parents[number] depends on the position of this file in a package
# its better to setup a seperate file call pathsetup.py in each sub directories with different "number"
# and just "import pathsetup" manually
path_root = Path(__file__).parents[number]

# convert path_root object to string and append into system path aka sys.path
sys.path.append(str(path_root))

# display the outcome
print(sys.path)
