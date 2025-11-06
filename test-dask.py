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
    c = distributed.Client('tcp://129.21.123.64:8786') # Chongzhou
    # c = distributed.Client('tcp://172.31.246.35:8786') # Wei
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob124")
    futures = c.submit(linpack2, random.randint(1,10000), user_id="bob124")
    futures = c.submit(linpack3, random.randint(1,10000), user_id="bob124")
    futures = c.submit(linpack4, random.randint(1,10000), user_id="bob125")
    futures = c.submit(linpack5, random.randint(1,10000), user_id="bob126")
    futures = c.submit(linpack6, random.randint(1,10000), user_id="bob127")