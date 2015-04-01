#!/usr/bin/env python

import sys

for line in sys.stdin:
    w = int(line[:-1])
    if (w > 3 and w % 2 == 0):
        print 'YES'
    else:
        print 'NO'

