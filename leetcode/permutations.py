class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        def backtrack(subset,nums):
            if len(subset)==len(nums):
                res.append(subset)
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    new=subset[:]
                    new.append(nums[i])
                    backtrack(new,nums)
                    visited.remove(i)
        backtrack([],nums)
        return res
                


            