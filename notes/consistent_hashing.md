# Consistent Hashing in Load Balancing

Source: https://youtu.be/zaRkONvyGr8

- when we add a node to a cluster, we want the new load sent to it to be equally partitioned out of every one of the other nodes
  - this ensures that the overall change within the old nodes are minimized
  - this means less data migrations, amongst other things
- we have to use consistent hashing to do this

## Consistent Hashing
- imagine a cyclic array of size 
- servers are uniformly random hashed to a positon in this array, such that they are distributed evenly and equally in the array
- when a request comes in, we hash it to a location into the ring, and we move to the clockwise nearest server
- the hashing is uniformly random -> the servers are distributed uniformly -> the requests are distirbuted uniformly -> the load is uniform
  - this means that on average, the load factor is just 1/M
- when we insert a new server into the ring, only the load of one other node is affected, since the load travels in a clockwise direction in the ring
- in an ideal world with high amounts of servers, you'd have a perfect 1/M load factor on every node, but when you have less nodes, there's a higher chance of a skewed distribution
- to avoid this potential skewed distribution, you just add more hash functions, `k` hash functions, which can place references of the node in more places in the ring
  - this way, each server node will exist in k places in the ring, so if one server dies, the load is distributed amongst the others
- on the other hand, if you add a server, load is equally reduced off other nodes, and added onto the new node
