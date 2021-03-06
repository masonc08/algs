# Eulerian Path
- eulerian path is a path of edges that visits all edges in a graph exactly once
- eulerian circuit is an eulerian path that starts and ends on the same vertex
  - this would mean that you can start the circuit at any node
- for directed graphs:
  - to have eulerian circuit, each vertex needs to have equal in and out degrees
  - to have eulerian path, at most one vertex has out-indegree=1, and in-outdegree=1
    and all other vertices have equal in and out degrees
- for undirected graphs:
  - to have eulerian circuit, each vertex needs an even degrees
  - to have eulerian path, every vertex needs even degree or exactly two vertices
    have odd degrees
- any eulerian circuit also contains an eulerian path
- use hierholzer's algorithm to discover eulerian paths after a eulerian path or 
  circuit has been verified
  - modified DFS algorithm that traverses all available edges instead of nodes