from collections import Counter

class Solution:
    def subarraySum(self, nums, k):
        dictionary = Counter()
        prefix = 0
        c = 0
        temp = 0
        dictionary[0] = 1 
        for i in range(len(nums)):
            prefix += nums[i]
            c += dictionary[prefix - k]  
            dictionary[prefix] += 1 
        return c
