#!/usr/bin/python
import random
import time
from dask.distributed import Client, wait

# -------- Workloads (simple print-only) -------- #

def chameleon(data, user_id=None):
    print("chameleon!", data)

def floatoperation(data, user_id=None):
    print("floatoperation!", data)

def jsondumpsloads(data, user_id=None):
    print("jsondumpsloads!", data)

def linpack(data, user_id=None):
    print("linpack!", data)

def matmul(data, user_id=None):
    print("matmul!", data)

def pyaes(data, user_id=None):
    print("pyaes!", data)

def imageprocessing(data, user_id=None):
    print("imageprocessing!", data)

def startup(data, user_id=None):
    print("startup!", data)


WORKLOAD_FUNCS = {
    "chameleon": chameleon,
    "floatoperation": floatoperation,
    "jsondumpsloads": jsondumpsloads,
    "linpack": linpack,
    "matmul": matmul,
    "pyaes": pyaes,
    "imageprocessing": imageprocessing,
    "startup": startup,
}

# -------- Experiment driver -------- #

if __name__ == "__main__":
    # Connect to your scheduler (DoubleDip or vanilla)
    client = Client("tcp://155.98.38.148:8786")  # adjust as needed

    NUM_USERS = 5
    NUM_TASKS = 500
    USERS = [f"user-{i}" for i in range(NUM_USERS)]
    WORKLOAD_TYPES = list(WORKLOAD_FUNCS.keys())

    random.seed(42)

    futures = []
    meta = []  # (task_key, user_id, workload_type)

    t0 = time.time()

    for i in range(NUM_TASKS):
        user_id = random.choice(USERS)
        workload_type = random.choice(WORKLOAD_TYPES)
        func = WORKLOAD_FUNCS[workload_type]

        data = random.randint(1, 10000)

        # key encodes user + workload + index
        task_key = f"{user_id}-{workload_type}-{i}"

        fut = client.submit(
            func,
            data,
            user_id=user_id,   # scheduler uses this
            key=task_key,      # good for log analysis
            pure=False,
        )

        futures.append(fut)
        meta.append((task_key, user_id, workload_type))

    wait(futures)
    t1 = time.time()

    print(f"Submitted {NUM_TASKS} tasks from {NUM_USERS} users.")
    print(f"Total runtime: {t1 - t0:.2f} seconds")

    # Save mapping for later joining with scheduler logs
    with open("client_task_meta.csv", "w") as f:
        f.write("task_key,user_id,workload_type\n")
        for key, uid, wtype in meta:
            f.write(f"{key},{uid},{wtype}\n")

    print("Wrote client_task_meta.csv")
