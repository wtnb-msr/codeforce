#!/usr/bin/env python

import sys


def plus_kv(dic, key, value):
    if key in dic:
        dic[key] += value
    else:
        dic[key] = value


def minus_kv(dic, key, value):
    if key in dic and dic[key] >= value:
        dic[key] -= value
        return True
    else:
        return False


def turn_case(s):
    return s.lower() if s.isupper() else s.upper()


def solve():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    messages = dict()
    availables = dict()
    for si in s:
        plus_kv(messages, si, 1)
    for ti in t:
        plus_kv(availables, ti, 1)

    count_yay = 0
    for si, si_count in messages.items():
        count_success = 0
        for i in range(si_count):
            is_success =  minus_kv(availables, si, 1)
            if is_success:
                count_yay += 1
                count_success += 1
        minus_kv(messages, si, count_success)

    count_whoops = 0
    for si, si_count in messages.items():
        si_turn = turn_case(si)
        count_success = 0
        for i in range(si_count):
            is_success =  minus_kv(availables, si_turn, 1)
            if is_success:
                count_whoops += 1
                count_success += 1
        minus_kv(messages, si, count_success)

    print count_yay, count_whoops


if __name__ == '__main__':
    solve()

