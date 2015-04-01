#!/usr/bin/env python

import sys

m, n = map(int, sys.stdin.readline().split(' '))

num_pieces = (m * n) / 2

print num_pieces
