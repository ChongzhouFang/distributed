## An Implementation of OpenWhisk Scheduling Algorithm in Dask
Changing ```./distributed/scheduler.py```

Potential Classes and Methods to Change:
```
├── TaskState
│   ├── ...
│   └── ...
├── SchedulerState
│   ├── decide_worker_rootish_queuing_disabled
│   ├── decide_worker_rootish_queuing_enabled
│   ├── decide_worker_non_rootish
│   ├── check_idle_saturated
│   ├── valid_workers
│   ├── worker_objective
│   ├── decide_worker
│   └── (end task?)
├── Scheduler
│   ├── decide_worker
```

Also need to maintain the list of function hosts on each machine.

In our setting:

1. Each function invocation is an HTTP request (tentatively ```curl```)
2. Schedules like normal dask jobs
3. When deploying: if there is no corresponding function host, need to fetch the function code (possibly store somewhere on the internet) and run ```dotnet run ...``` before executing the ```curl``` command

So we need to change the part to run code as well.
```
scheduler.py
├── SchedulerState
│   ├── _add_to_processing

worker.py
├── async run
├── class worker (add a list of currently running hosts; add logic to determine how to wrap function)
│   ├── run()
```



Actual Changes:
Inside
```
""""""""""""""""""""""""""""""""""""""""""
"             Changes start.             "
""""""""""""""""""""""""""""""""""""""""""
```
and
```
""""""""""""""""""""""""""""""""""""""""""
"             Changes end.               "
""""""""""""""""""""""""""""""""""""""""""
```

Change lists:
```
scheduler.py
├── Added utility functions gcd(), pairwiseCoprimeNumberUtil()
├── TaskState: add element schedule_hash (problem: where is the key generated?)
│   ├── Added function generate_schedule_hash()
│   ├── Added definition of schedule_hash to __init__()
├── WorkerState: add element running_hosts to store currently running function host instances
├── SchedulerState:
│   ├── Modify function new_task()
│   ├── Modify function decide_worker_rootish_queuing_disabled()
│   ├── Modify decide_worker_rootish_queuing_enabled()(add param ts)
│   │   (Related changes, add param ts when being invoked)
│   │   ├── Modify transition_waiting_processing()
│   │   ├── Modify transition_queued_processing()
│   ├── Modify decide_worker_non_rootish()


worker.py
├── modified async run() function
├── Worker: 
│   ├── Added element running_instances
│   ├── Added member function add_instance()
```
