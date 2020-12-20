class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def solve(S):
            if s<0:
                return 0
            sol = i = 0
            for j, v in enumerate(A):
                S -= v
                while S < 0:
                    S += A[i]
                    i += 1
                sol += (j-i+1)
            return sol
        return solve(S)-solve(S-1)
    
        # i = j = cur = 0
        # sol = 0
        # while j < len(A) and cur < S:
        #     cur += A[j]
        #     j += 1
        # while j < len(A):
        #     a = i
        #     while i < len(A) and A[i] != 1:
        #         i += 1
        #     if A == len(A):
        #         return len(A)*(len(A)-1)//2
        #     b = j
        #     j += 1
        #     while j < len(A) and A[j] == 0:
        #         j += 1
        #     sol += ((i-a+1)*(j-b))
        #     i += 1
        # return sol