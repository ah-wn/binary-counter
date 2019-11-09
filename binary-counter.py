from time import sleep
from itertools import count

i, o = '|_'
i, o = '._'
for u in count():
    u = bin(u)[2:].replace('0', i).replace('1', o)
    print(len(u), u, end='\r', flush=1)
    # sleep(.000001)
