# Rename all files in directory

import os
for filename in os.listdir("."):
    if filename.startswith("Comp424-"):
        os.rename(filename, filename[8:])
