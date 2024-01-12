class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        for j in range (len(nums)):
            if nums[j]!=val:
                  nums[count]=nums[j]
                  count+=1
        print(nums,len(nums))
        return count
nums = [1, 2, 3, 4,5,5,5]

val=5
Solution().removeElement(nums,val)