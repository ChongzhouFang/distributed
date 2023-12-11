import dask
import distributed
import os

def warmup():
    pass

if __name__ == '__main__':
    c = distributed.Client('tcp://192.168.1.111:8786')
    futures = c.submit(warmup, None)