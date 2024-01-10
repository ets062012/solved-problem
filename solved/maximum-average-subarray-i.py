class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=0
        current_sum=0
        max_sum=-float('inf')
        
        while r<len(nums):
            if r-l+1==k:
                current_sum+=nums[r]
                max_sum=max(current_sum/k,max_sum)
                
                current_sum-=nums[l]
                l+=1
                r+=1
                pass
            else:
                current_sum+=nums[r]
                r+=1
        return max_sum



        