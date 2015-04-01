#!/usr/bin/env python

import sys

origin = sys.stdin.readline().rstrip()

vowels = set(['a', 'A', 'o', 'O', 'y', 'Y', 'e', 'E', 'u', 'U', 'i', 'I'])

ans = [ '.' + c.lower() for c in origin if c not in vowels ]

print ''.join(ans)

