# Trees and Graphs
- complete binary trees are filled always from left to right, eg: heap
- full binary trees have every node in them have either zero or two children
- perfect binary trees have exactly 2^k-1 nodes and all leaves are on the same level
- in order traversal of bst gives nodes in ascending order
- popping from heap removes top element from tree and replaces it with last item at bottom of heap
  - new top element is sunk down by swapping with smallest/largest of two children depending on 
    max or min heap
- pushing to heap adds to last slot at bottom, new element is surfaced up until the parent is 
  larger/smaller than itself depending on max or min heap
- tries are an n-ary tree of characters where every path down the tree reprsents a word
  - can have up to the number of alphabets as its children, not including termination node
- use special termination nodes to represent termination of a word, or add a flag to the parent
- used to lookup prefixes within a set of words in O(K) time, k=len(prefix)
  - same runtime as hashmap access since hashmap needs to read the string too
- trees are a connected, directed, acyclic graph
- a graph is connected if there is a path between every pair of possible nodes
- DFS searches a branch completely before swapping to the next, go deep before going wide
- BFS searches all neighbors before going to any of their children, go wide before going deep
- DFS simpler for basic graph traversal
- BFS is ideal for shortest path or pathfinding between two nodes
  - DFS can't find shortest path easily
- pre-order tree traversals are DFS
- bidirectional search performs bfs from source and destination nodes to find shortest path
  - connect paths on search collision to identify shortest path
- BFS identifies shortest path in O(k^d), bidirectional identifies in O(k^(d/2)), k is number 
  of neighbors per node, d is shortest path distance between two nodes in concern
- prim's algorithm generates minimum spanning tree by always taking shortest cost edge to connect
  all nodes together
  - consists of a connected cloud and a non-connected cloud, alg tries to connect all together
- kruskal's algorithm generates minimum spanning tree by picking lowest cost edges that connects
  a previously unconnected vertice
- strongly connected components have every vertice accessible from every other vertice
- kosaraju's algorithm for strongly connected component searches for strongly connected 
  components
  - dfs and push fully explored nodes into stack, reverse all edges, perform dfs using nodes in 
    order of stack, connected components are strongly connected components
- topologically sort a graph by using dfs and pushing into a stack once it's fully explored, 
  stack holds the topologically sorted graph, least dependent at top of stack
- detect loops in directed graphs using dfs, if callstack arrives at node already in callstack, 
  then there is cycle
- djikstra's algorithm searches for shortest path between two nodes
  - store all nodes into list with key of infinity, excluding starting node with key of 0
  - initialize node -> prev_node map and node -> distance map
  - pop smallest node out of list, set new distance of adjacent vertices in list, node -> 
    distance map, and add the parent node to node -> prev_node map
  - when all nodes in list is empty, find distance of the node you want in node -> distance map
  - to find the shortest path, use the node -> prev_node map to backtrack the path