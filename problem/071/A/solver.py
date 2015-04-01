#!/usr/bin/env python

import sys
import os

n = int(sys.stdin.readline())

for line in sys.stdin:
    word = line[:-1]
    length = len(word)
    if (length > 10):
        first_char = word[0]
        last_char = word[length - 1]
        abbreviation = first_char + str(length - 2) + last_char
        print abbreviation
    else:
        print word


