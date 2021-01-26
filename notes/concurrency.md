# Concurrency
Source: https://www.youtube.com/watch?v=LOfGJcVnvAk
https://www.youtube.com/watch?v=FChZP09Ba4E
Parallelism is a lot of things happening at once, concurrency is about dealing with a lot of things at once...

## Threads
- a program under exection is a process
- thread is a basic unit of execution
- each program can have many processes
- each process can have multiple threads
- a thread is a basic unit of CPU unitilization
- a thread is made of a thread ID, a program counter, a register set, and a stack, every thread has one of these
- threads share resources with each other
- if a process has multiple threads of control, it can perform more than one task at a time
- ![threads](https://i.imgur.com/5lhS4pO.png)
- Eg. Chrome is a process, which has multiple threads running
  - one thread for downloading, one for display, so we can do both atthe same thing
- there's 4 major benefits of multithreadding
  - responsiveness: a program can keep running even if part of it is blocked or performing a difficult operation
  - resource sharing: threads share memory and resources from the process. This allows an application to have lots of threads of activity in the same address space, very efficient since there's no need for dedicated resources
  - economy: since threads share resources of the process, it's cheap to create and context-switch threads
  - utilization of multiprocessor achitecture: on multiprcessors, threads can run in parallel on different processors, increasing concurrency
- scheduler schedules threads onto different CPU cores
- so if you have 4 CPUs and 4 threads, they can all run at once
- when there's only one CPU, scheduler will swap between allowing each thread to run for a non-deterministic amount of time
  - this creates problems as sometimes the thread may not complete its operation before it's halted by the scheduler
  - ![single_core_two_threads](https://i.imgur.com/Ssnm5lu.png)
- similar problem can happen with parallel threads on multiple cores
  - ![multi_core_two_threads](https://i.imgur.com/T8VIHXy.png)
- one possible way to fix this problem is to use locks and wrap the function with lock/unlock
- concurrency is generally useful when there's a shared resource that's accessed or updated, or multiple tasks need to be coordinated
  - manages state of a resource
