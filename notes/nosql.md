# NoSQL

Source: https://www.youtube.com/watch?v=xQnIN9bW0og

## NoSQL vs SQL
- retrievals take the entire JSON blob
- doesn't support easy data modification
  - not built for lots of data updates
  - sql usually has acid guarentee, nosql doesn't guarentee
  - finances wont use nosql because of data guarentee
- schema-less
- adding new data to SQL requires locks to maintain consistency, which is expensive
  - in nosql, you just add another key to the json
- nosql has horizontal partitioning built in, which is more focused on availibility
- a lot of the times, availability > consistency
- nosql is much better for metrics and intelligent data (smart aggregations)
- nosql is slower at reading than sql
- there's no way to do a foreign key constraint within nosql, since there's no easy way to do joins
  - when you have two nosql tables, doing a join is incredibly slow, no optimization

### Situations to use NoSQL
- lots of writes... NoSQL is write optimized
- need aggregations for metrics

## Cassandra Architecture Example
- inputs are hashed based on a mod upon their request ID
- there are 5 cassandra instances in a cluster, hashing keys 0-499
- ![example](https://i.imgur.com/q9AbqU9.png)
- if your hash function is bad, you can make a two layer cluster
  - in case one node cant take the load, the request is sent to the second layer cluster
  - run it through another hash function that is better distributed
  - multiple levels of hashing/sharding
  - eg: if you're hashing off a country ID, a country can cause a lot of stress on a node
  - introducing another level of clusters will relieve this stress
- while we send data to only one node based on what the hash gives us, we also dont want to lose any data if the node we send our data to goes down
- one solution to this problem is to get the next node in the cycle to store a copy of the original node's data (Replication factor = 2)
  - this also allows more than one replica to answer a read query
- this gives the cassandra cluster better load balancing and replication of data
- if replication factor is 3, when you write on 5 you also concurrently write on 1 and 2
  - consider if 1 and 2 are slow and dont get the write in time, and only 5 got the write
  - if 5 crashes before 1 and 2 get the write, the data not exist when it is read
- we can create an agreement on the existence of data through a quorum
  - multiple nodes who are responsible for a piece of data agree on a data values that exists
  - if quorum=2, then if 2 out of the 3 nodes come to the same agreement that the data doesnt exist, then the information will be surfaced to the requesting user
- cassandra writes requests in a log file, which uses efficient appending
  - it keeps a pointer to where the end of the log is, and it just appends write queries to it
- logs are periodically dumped into a SST (sorted string table) for persistent storage, a table of kv pairs where the keys are sorted
  - data in this table is immutable, and it's merged on occasion in order to save space in the node
