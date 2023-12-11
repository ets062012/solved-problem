class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums)):
           for j in  range(i,len(nums)):
               s=nums[i]+nums[j]
               if s==target:
                   if i!=j:
                       return [i,j]
                


        