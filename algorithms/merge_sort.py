"""
A series of exercises, implementing various styles of merge sorting algorithms
"""

class MergeSort:
    # Recursive merge sorting, O(nlogn) runtime, O(n) space for recursion
    @staticmethod
    def recursive(li, i=None, j=None):
        if len(li) == 0:
            return li
        if not i and not j:
            i, j = 0, len(li)
        if j-i == 1:
            return [li[i]]
        mid = (i+j)//2
        MergeSort.recursive(li, i, mid)
        MergeSort.recursive(li, mid, j)
        MergeSort._merge(li, i, mid, j)


    # Iterative bottom-up merge sorting, O(nlogn) runtime, O(n) space
    @staticmethod
    def iterative(li):
        if len(li) <= 1:
            return li
        size = 1
        while size <= len(li):
            size *= 2
            i = 0
            while i < len(li):
                end = min(i+size, len(li))
                MergeSort._merge(li, i, (i+size+i)//2, end)
                i = end
        return li


    # Merge sorted subarrays [i, mid) and [mid, j) in-place
    @staticmethod
    def _merge(li, start, mid, end):
        left, right = li[start:mid], li[mid:end]
        i, j = 0, 0
        while i < len(left) or j < len(right):
            if j == len(right):
                li[start+i+j] = left[i]
                i += 1
            elif i == len(left):
                li[start+i+j] = right[j]
                j += 1  
            elif left[i] < right[j]:
                li[start+i+j] = left[i]
                i += 1
            else:
                li[start+i+j] = right[j]
                j += 1
