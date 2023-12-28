class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
    
        for i in range(len(nums)):
            count = sum(1 for num in nums if num < nums[i])
            result.append(count)
    
        return result


        