# Fenwick Tree
- source: https://www.youtube.com/watch?v=CWDQJGaN1gY

- used to get prefix sum of aray
  - Fenwick tree is another way of solving this problem without using prefix sums
- However, prefix sums does not adapt well when there are changes in the original array, since you need O(n) time for every update to update the prefix sum array
- You can also use segment trees to solve this problem, but it is less optimal compared to fenwick trees
- O(n) space to store Fenwick tree, O(logn) to query, O(logn) to update, O(nlogn) to create fenwick tree
- fenwick tree holds n+1 elements, precisely 1 more element than the initial array
  - 0 is a dummy node in the tree, other elements store prefix sum
![example](https://i.imgur.com/1m0UCYz.png)
- each node's parent is the node's index's set LSB inverted
  - eg. 10=0b1010, LSB flipped is 0b1000=8, indicating that 8 is the parent of 10
  - ![example](https://i.imgur.com/IDQsIEn.png)
- each index in the tree holds cumulative sum of `(index-1)-last_set_LSB` to `index-1`
- ![example](https://i.imgur.com/FIhPQxU.png)
- to query index i, sum up index i, index i with 1 set LSB removed, index i with 2 set LSB remove, ... until there are no more set LSBs
  - eg: querying 0 to 5: start at node 5+1=6=0b110, then 4=0b100, then 0=0b0, and add all these together
- to traverse up the tree, we remove the last set LSB
- remove last set LSB quickly by applying any of the formulas to remove one LSB: `n&(n-1)` or `n-(n&~n)`
- to move to the "next" node on the tree, move the set group LSB left by one, this can be done by `n+(n&~n)`
- populate fenwick tree nodes by adding the new sum to the index and all its "next" values that are within the range of the array
