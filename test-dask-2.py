#!/usr/bin/python
import dask
import distributed
import os
import random

def warmup(data):
    print(
        "Warming up!",
        data
    )

def linpack(data):
    print(
        "Linpack!",
        data
    )

def linpack2(data):
    print(
        "Linpack!",
        data
    )

def linpack3(data):
    print(
        "Linpack!",
        data
    )

def linpack4(data):
    print(
        "Linpack!",
        data
    )

def linpack5(data):
    print(
        "Linpack!",
        data
    )

def linpack6(data):
    print(
        "Linpack!",
        data
    )

if __name__ == '__main__':
    # c = distributed.Client('tcp://129.21.123.64:8786') # Chongzhou
    c = distributed.Client('tcp://192.168.4.64:8786') # Wei
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob124") # 1 first task
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob124") # 2 same task, same user
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob125") # 3 same task, different user
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob126") # 4 same task, another different user
    futures = c.submit(linpack2, random.randint(1,10000), user_id="bob124") # 5 different task, same user
    futures = c.submit(linpack2, random.randint(1,10000), user_id="bob127") # 6 different task, different user

    # epected behavior (3 workers):
    # first two tasks should go to the same worker
    # third task should go to a different worker
    # fourth task should go to a different worker other than previous two
    # fifth task should go to the same worker as first two tasks
    # sixth task should go to a any worker other than the worker with first user it has two users, while other two workers have one user each.