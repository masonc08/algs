# Floyd-Warshall

- Source https://www.youtube.com/watch?v=oNI0rf2P9gE

- DP graph algorithm used to find shortest path between all pairs of vertices in a directed graph
- Select a vertice and find shortest path from itself and all it neighbors, using a DP cache to save computation across vertices
- create adjacency matrix to record weights between two vertices
![example](https://i.imgur.com/l0ciZDI.png)
- if there is no edge going to and from the same vertice, record its weight as 0
- if there is no edge going from vertex A and vertex B, record its weight as infinity
- given initial adjacency matrix, for each vertex, check if any paths can be minimized by going through the chosen vertex
- Eg. We know that there is a path from 2 to 3, but there may be a shorter path from 2 to 3 by first going through vertex 1
  - perform this by `max(prev[2][3], prev[2][1]+prev[1][3])`
  ![example](https://i.imgur.com/6I3rX9j.png)
- Leave the paths involving the chosen vertex as they were
- overall O(n^3) runtime, which is actually no better than repeating Djikstra's algorithm n times for every vertex, but Floyd-Warshall actually still runs faster due to DP caching
