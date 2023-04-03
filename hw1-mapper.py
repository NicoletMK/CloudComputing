#!/usr/bin/env python
from csv import reader
import sys

for line in reader(sys.stdin):
    
    boro,crime = (line[13].strip(), line[7].strip())
    if not boro or not crime:
        continue
    else:
        print('%s\t%s\t%s' % (boro,crime,1))     

