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