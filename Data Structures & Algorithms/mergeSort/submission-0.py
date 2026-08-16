# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs: List[Pair], s: int, m: int, e: int) -> None: 
        # in-place merge, return nothing

        # Create copies of halves
        L = pairs[s : m + 1]
        R = pairs[m+1:e+1]

        i = j = 0 # pointers for L and R copies of pairs
        k = s     # pointer for original array

        # Compare and merge
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key: # <= indicates stability of sorting
                pairs[k] = L[i]
                i += 1
            else: 
                pairs[k] = R[j]
                j += 1
            k += 1

        # Copy leftover elements
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # Base Case of single element
        if e - s + 1 <= 1:
            return pairs
        
        # find middle index to partition at
        m = s + (e-s) // 2

        #Recursively sort left half
        self.mergeSortHelper(pairs, s, m)

        #Recursively sort right half
        self.mergeSortHelper(pairs, m + 1, e)

        # merge sorted halves
        self.merge(pairs, s, m, e)

        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # edge case
        if len(pairs) == 0:
            return pairs

        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

