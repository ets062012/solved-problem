class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        i = 1
        
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if c == 1:
                    return False
                if i >= 2 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                c += 1
            i += 1
        
        return True
       


        