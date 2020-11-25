from typing import List
from collections import defaultdict


class Djikstra:
    """
    Given...
    - a directed acyclic graph consisting of vertices [0, n), 
    - a list of weighted edges [a, b, w] indicating a directed edge from a to b,
      with a weight of w
    - origin vertice u, and destination vertice v,
    return the shortest path from vertice u to v
    """
    def shortest_path(self, n: int, edges: List[List[int]], u: int, v: int) -> List[int]:
        dist = [0x7fffffff]*n
        dist[u] = 0
        prev = [None]*n
        not_visited = dict(enumerate(dist))
        adj_list = defaultdict(set)
        for a, b, w in edges:
            adj_list[a].add((b, w))
        while not_visited:
            node = min(not_visited, key=not_visited.get)
            for nbr, w in adj_list[node]:
                cur = dist[node]+w
                if cur < dist[nbr]:
                    dist[nbr] = cur
                    not_visited[nbr] = cur
                    prev[nbr] = node
            del not_visited[node]
        sol = []
        runner = v
        while runner:
            sol.append(runner)
            runner = prev[runner]
        sol.append(u)
        sol.reverse()
        return sol

class Assert(Djikstra):
    def __init__(self):
        edges = [
            [0, 1, 1],
            [0, 2, 5],
            [1, 2, 2],
            [1, 3, 2],
            [1, 4, 1],
            [2, 4, 2],
            [3, 4, 3],
            [3, 5, 1],
            [4, 5, 2]
        ]
        assert self.shortest_path(6, edges, 0, 5) == [0, 1, 4, 5]

Assert()
