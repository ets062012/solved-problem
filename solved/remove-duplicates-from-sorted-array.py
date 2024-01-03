class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        
        
        for i in range(1, len(nums)):
            if nums[l]!=nums[i]:
                nums[l+1],nums[i]=nums[i],nums[l+1]
            
                l+=1
                
        return l+1


        