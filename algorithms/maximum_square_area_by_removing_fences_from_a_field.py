from typing import List


class Solution:
    def maximizeSquareArea(self, n: int, m: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1), vFences.append(1)
        hFences.append(n), vFences.append(m)
        hFences.sort(), vFences.sort()
        h_sizes, v_sizes = [], set()
        for i, h0 in enumerate(hFences):
            for j in range(i+1, len(hFences)):
                h_sizes.append(hFences[j]-h0)
        for i, v0 in enumerate(vFences):
            for j in range(i+1, len(vFences)):
                v_sizes.add(vFences[j]-v0)
        h_sizes.sort(key=lambda v: -v)
        for h in h_sizes:
            if h in v_sizes:
                return (h*h)%(10**9+7)
        return -1
        
