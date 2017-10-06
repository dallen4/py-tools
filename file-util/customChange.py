# Rename all files in directory

import os
for filename in os.listdir("."):
    charTarget = filename.find("-")
    i = charTarget+1
    os.rename(filename, filename[i:])
