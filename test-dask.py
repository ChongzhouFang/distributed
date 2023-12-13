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

if __name__ == '__main__':
    c = distributed.Client('tcp://192.168.1.111:8786')
    futures = c.submit(warmup, random.randint(1,10000))