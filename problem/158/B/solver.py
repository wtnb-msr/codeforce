#!/usr/bin/env python

import sys

num_groups = int(sys.stdin.readline().rstrip())

num_group_count = [ 0, 0, 0, 0 ]

groups = map(int, sys.stdin.readline().rstrip().split(' '))

for group in groups:
    num_group_count[ group - 1 ] += 1

num_taxies = 0

# 4
num_taxies += num_group_count[3]
num_group_count[3] = 0

# 3 + 1
num_taxies += num_group_count[2]
if (num_group_count[2] >= num_group_count[0]):
    num_group_count[0] = 0
    num_group_count[2] = 0
else:
    num_group_count[0] -= num_group_count[2]
    num_group_count[2] = 0

# 2 + 2 or 2 + 1 + 1
num_taxies += num_group_count[1] / 2
num_group_count[1] %= 2

num_taxies += num_group_count[1]
if (num_group_count[1] * 2 >= num_group_count[0]):
    num_group_count[0] = 0
    num_group_count[1] = 0
else:
    num_group_count[0] -= num_group_count[1] * 2
    num_group_count[1] = 0

# 1 + 1 + 1 + 1
num_taxies += num_group_count[0] / 4
if (num_group_count[0] % 4 > 0):
    num_taxies += 1

num_group_count[0] = 0

# check
for i in num_group_count:
    if i > 0:
        print 'invalid'

print num_taxies
