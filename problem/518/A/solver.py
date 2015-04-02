#!/usr/bin/env python

import sys


def diff_char(s, t):
    return int(ord(s) - ord(t))


def is_diff_more1(s, t):
    length = len(s)
    for i in range(length):
        s_i = s[i]
        t_i = t[i]
        if (i == length - 1):
            if (diff_char(t_i, s_i) > 1):
                return True
        else:
            if (diff_char(t_i, s_i) > 0):
                return True


def increment_char(s):
    if (s == 'z'):
        return (True, 'a')
    else:
        return (False, str(unichr(ord(s) + 1)))


def increment_str(s):
    length = len(s)
    for i in range(length - 1, -1, -1):
        is_propagated, s[i] = increment_char(s[i])
        if not is_propagated:
            return


def solve():
    s = list(sys.stdin.readline().rstrip())
    t = list(sys.stdin.readline().rstrip())
    if is_diff_more1(s, t):
        increment_str(s)
        if s != t:
            print ''.join(s)
            return

    print 'No such string'
    return



if __name__ == '__main__':
    solve()

