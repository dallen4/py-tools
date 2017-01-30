# Rename all files in directory

import os
for filename in os.listdir("."):
    if filename.startswith("Copy of "):
        os.rename(filename, filename[8:])
