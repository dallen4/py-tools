#order contestants randomly
import os
import random

conList = ['Ossai', 'Tessy [drums]', 'Tessy', 'Efe', 'Blessing', 'Favour', 'Helen', 'Raymond', 'Chidima', 'Okusgirl']
random.shuffle(conList)

for contestant in conList:
    print(contestant)
