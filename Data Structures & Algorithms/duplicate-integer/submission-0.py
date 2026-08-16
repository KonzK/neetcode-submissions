from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = Counter(nums)
        for num in nums:
            if hashset[num] != 1:
                return True
        return False