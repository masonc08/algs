class Solution:
    """
    Two-passing up to sqrtn
    Runtime: 28 ms, faster than 87.05% of Python3 online submissions for The kth Factor of n.
    Memory Usage: 14.3 MB, less than 13.74% of Python3 online submissions for The kth Factor of n.
    """
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        while i*i <= n:
            if n%i == 0:
                k -= 1
                if k == 0:
                    return i
            i += 1
        i -= 1
        if i*i == n:
            i -= 1
        while i > 0:
            if n%i == 0:
                k -= 1
                if k == 0:
                    return n//i
            i -= 1
        return -1


    """
    Linear scanning
    Runtime: 36 ms, faster than 25.30% of Python3 online submissions for The kth Factor of n.
    Memory Usage: 14.3 MB, less than 13.74% of Python3 online submissions for The kth Factor of n.
    """
    # def kthFactor(self, n: int, k: int) -> int:
    #     for i in range(1, n+1):
    #         if n%i == 0:
    #             k -= 1
    #         if k == 0:
    #             return i
    #     return -1
