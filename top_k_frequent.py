def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    occurrences = {}
    for num in nums:
        occurrences[num] = occurrences.get(num, 0) + 1
    sol = [None]*k
    for i in range(k):
        largest = (None, 0)
        for key, value in occurrences.values():
            if value > largest[1]:
                largest = (key, value)
        sol[i] = largest[0]
        del occurrences[largest[0]]
    return sol
