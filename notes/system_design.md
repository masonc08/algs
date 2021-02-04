# System Design
Source: <https://blog.pramp.com/how-to-succeed-in-a-system-design-interview-27b35de0df26>

- system design problems will often have multiple solutions, each having upsides and downsides
- it's important to know about tools that exist to solve a particular problem, even if you've never seen one

## Steps to solve a system design problem
### Understand the Goals
- clearly define and share with the interviewer the end goals of the system!
- start by questioning the most basic goals, like what the system is meant to acheive, who are the users of the system, what the users need the system for, and how they'll use it
- think about what the system should input and output

### Establish the Scope
- Share and define all the features you think that will be useful for the user, and make sure the interviewer agrees with your scope
- should the design be just for the API? What type of clients (mobile, web, ..)are there? is there authentication, analytics, or integrations involved?

### Design for the Right Scale
- software will be designed differently depending on the scale of users it supports
- are we going to be able to support all the reads on one machine, or do we need to think about scaling?
- what is the expected read-to-write ratio? how many concurrent requests should we expect? what is the average expected response time? what is the limit on the data users can provide?

### Start High-Level, then Drill-Down
- Start by covering what you need to do to cover the product end to end at a high level (MVP)
- define what the system's entry points are, is it from a direct user interaction, or from an API call?
- after the base has been built, start iterating on the system and identify optimizations you can make for performance bottlenecks, and task separation
- think about sharding dbs, or how you plan on horizontally scaling services with a load balancer to handle more load

### Data Structures and Algorithms
- think about the algorithms you'll need to use to do any data parsing/conversions
- what kind of hashing function will you use for a URL shortner? What kind of algorithms will you run to get certain analytics? what kind of function will you run to get the most helpful article recommendations for a user?
- identify runtime and space complexities for any algorithms

### Tradeoffs
- a lot of decisions you make will have another alternative to them
- mention alternate solutions and their tradeoffs
- if you can mention tradeoffs in realtime as you suggest solutions, it shows that you understand complex systems require compromises and nothing is perfect
- this is really important since ultimately there is no correct answer to system design problems
- Eg: what kind of DB are you going to use? SQL? NoSQL? What are the tradeoffs? What kind of caching servise will you use? Redis? memcached? What are the tradeoffs between the two? What kind of frameworks will you use?

## System Design Patterns

### Messaging Queue
<https://youtu.be/oUJbuFMyBDk>

- clients make a request and immediately returns a promise
- requests are thrown into a queue, and removed as they are processes
- this allows the CPU to complete tasks according to a priority
- this is considered as asynchronous processing
- however, if one node goes down, all the data within its queue are lost, when it should really just be sent to aother node that is still operational, in order to complete the task at the broken node
- we can consider storing tasks within a database such that the data persists, without remembering which node the task came from
- create a heartbeat service to check if node status on intervals, if it notices that a service is dead, it queries the database for uncompleted orders and distributes it to the remaining alive servers
- to distribute the abandoned tasks to the remaining alive servers, we use a load balancer to equally distribute the tasks from the lost nodes to the remaining alive nodes
- consistent hashing ensures that the same tasks that were queried from alive nodes are sent back to the same alive nodes, so we dont have duplication of tasks among two nodes
- rabbitMQ is a messaging queue

### Microservice vs Monolith
<https://youtu.be/qYhRvH9tJKw>

- how do you know when to use monoliths vs microservice?
- you can still horizontally scale a monolith
- a microservice is a single business unit, and services are isolated out to their smallest piece
- clients may connect to a gateway, and the gateway communicates the client with the microservices

#### Monoliths
- for small teams, monolith is good because it's easier to get things done
- simple maintenance and dont need to think as hard for deployments
- code just has to be written once since it's just one codebase
- monoliths are faster than microservices since calls are within the same system, theese are local calls vs microservices have to use network calls
- new developers need to know a lot of context on the codebase to start working
- monoliths are a single point of failure, if there's a mistake anywhere in the codebase, the entire monolith crashes

#### Microservices
- easiest to scale, it's a suite of services, which each service can be scales
- easier to design the system
- new team members just need to know the context of one microservice that they are working on
- parallel development is easier as working on different microservices are on different codebases
- microservices has better metrics, as you know exactly which part of the code is under higher load
- if a microservice is only talking to once service, then maybe they should be just put together
  - this reduces the need for RPC (network) calls

## Database Sharding
<https://youtu.be/5faMjKuB9bc>

- sharding takes one attribute into the data, and partition it such that each node gets one chunk of it
- we need to ensure data is still consistent with sharding
- we also need to ensure that the database is availability
- we can shard database on an ID, but sometimes there is better ways to shard such as using location, for location sensitive apps like tinder
  - this lets you query very fast, as the shards are indexed by the thing you're looking for
- we can create a master-slave architecture on each shard, to prevent loss when one shard goes out
  - writes are done to the master, reads are done to the slaves, and if the master goes out, one slave is promoted to the master

### Problems
- joining tables across shards is very difficult because now it involves network calls
- cant have dynamic number of shards
  - you can overcome this by sharding a shard recursively (hierarchical sharding)
- hard to make data consistent
