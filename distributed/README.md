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
│   └── decide_worker
│   └── (end task?)
├── Scheduler
│   ├── decide_worker
```

Actual Changes:
Inside
```
""""""""""""""""""""""""""""""""""""""""""
"             Changes   start.           "
""""""""""""""""""""""""""""""""""""""""""
```
and
```
""""""""""""""""""""""""""""""""""""""""""
"             Changes   end.             "
""""""""""""""""""""""""""""""""""""""""""
```

Change lists:
```
├── TaskState: add element schedule_hash (problem: where is the key generated?)
│   ├── Added function generate_schedule_hash()
```
