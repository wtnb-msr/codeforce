#!/usr/bin/env python

import sys
import os

num_partisipants = 0
k_th = 0

num_partisipants, k_th = map(int, sys.stdin.readline()[:-1].split(' '))
scores = map(int, sys.stdin.readline()[:-1].split(' '))

num_advancers = 0
k_th_score = scores[k_th - 1]

for i in range(0, len(scores)):
    if (scores[i] > 0):
        if (scores[i] >= k_th_score):
            num_advancers += 1
        else:
            break
    else:
        break

print num_advancers


