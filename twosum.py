class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if (i!=j and sum==target):
                    return [i, j]
                
        return[]