#!/usr/bin/env python

import sys
import os

for line in sys.stdin:
    n, m, a = map(int, line[:-1].split(' '))
    num_x = n / a
    num_y = m / a
    additional_x = 1 if (n % a > 0) else 0
    additional_y = 1 if (m % a > 0) else 0
    total = (num_x + additional_x) * (num_y + additional_y)
    print total

