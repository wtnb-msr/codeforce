#!/usr/bin/env python

import sys


def update_index(index_to_app, app_to_index, app_id, app_index):
    if (app_index > 0):
        pre_app_index = app_index - 1
        pre_app_id = index_to_app[pre_app_index]
        # update
        index_to_app[app_index] = pre_app_id
        index_to_app[pre_app_index] = app_id
        app_to_index[app_id] = pre_app_index
        app_to_index[pre_app_id] = app_index


def solve():
    num_apps, num_lunch, num_apps_screen = map(int, sys.stdin.readline().rstrip().split(' '))
    index_to_app = map(int, sys.stdin.readline().rstrip().split(' '))
    app_to_index = { index_to_app[i]:i for i in range(num_apps) }
    launched_apps = map(int, sys.stdin.readline().rstrip().split(' '))
    count_gestures = 0

    for app_id in launched_apps:
        app_index = app_to_index[app_id]
        screen_index = app_index / num_apps_screen
        count_gestures += screen_index + 1 # swipe + launch
        update_index(index_to_app, app_to_index, app_id, app_index)

    print count_gestures


if __name__ == '__main__':
    solve()

