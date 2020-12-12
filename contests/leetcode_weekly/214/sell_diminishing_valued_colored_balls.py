"""
Leetcode 1648
Leetcode weekly contest 214
"""


import heapq
from typing import List

class Solution:
    MOD = 10**9+7

    """
    O(NlogN) solution from sorting
    Runtime: 640 ms, faster than 96.31% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.
    Memory Usage: 25.4 MB, less than 6.04% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.
    """
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        sol = 0
        k = 1
        for i in range(len(inventory)-1):
            if inventory[i+1] != inventory[i]:
                if k*(inventory[i]-inventory[i+1]) <= orders:
                    diff = inventory[i]-inventory[i+1]
                    sol += k*self._cumu_diff(inventory[i+1], inventory[i])
                    orders -= k*diff
                    if orders == 0:
                        break
                else:
                    q, r = divmod(orders, k)
                    sol += k*self._cumu_diff(inventory[i]-q, inventory[i])
                    sol += r*(inventory[i]-q)
                    break
            k += 1
        return sol%self.MOD

    """
    TLE solution using heap
    """
    # def maxProfit(self, inventory: List[int], orders: int) -> int:
    #     inventory.append(0)
    #     for i in range(len(inventory)):
    #         inventory[i] = -inventory[i]
    #     heapq.heapify(inventory)
    #     sol = 0
    #     while orders:
    #         top = -heapq.heappop(inventory)
    #         peek = -inventory[0]
    #         items_to_sell = top-peek+1
    #         if items_to_sell > orders:
    #             sol += self._cumu_diff(top-orders, top)
    #             sol %= self.MOD
    #             top -= orders
    #             orders = 0
    #         else:
    #             sol += self._cumu_diff(peek-1, top)
    #             sol %= self.MOD
    #             top -= items_to_sell
    #             orders -= items_to_sell
    #         heapq.heappush(inventory, -top)
    #     return sol%self.MOD

    def _cumu_diff(self, lo, hi):
        return (hi*(hi+1)//2-lo*(lo+1)//2)%self.MOD

print(Solution().maxProfit([497978859,167261111,483575207,591815159], 836556809))