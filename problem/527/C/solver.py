#!/usr/bin/env python

import sys

width, height, num_cuts = map(int, sys.stdin.readline().lstrip().split(' '))

w_length_list = []

for i in range(num_cuts):
    token = sys.stdin.readline().lstrip().split(' ')
    cut_type = token[0]
    cut_position = int(token[1])
    print cut_type, cut_position

