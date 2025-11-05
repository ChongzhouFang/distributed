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

if __name__ == '__main__':
    c = distributed.Client('tcp://129.21.123.64:8786')
    futures = c.submit(linpack, random.randint(1,10000), user_id="bob124")