class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        prefix=0
        suffix=sum(nums)
        for i in range(len(nums)):
            suffix=suffix-nums[i]
           
            if prefix==suffix:
                return i
            else:
                prefix+=nums[i]
        return -1
        