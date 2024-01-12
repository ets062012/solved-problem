class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count=defaultdict(int)
        s=0
        l=0
        ans=0
        for r in range(len(nums)):
            s+=nums[r]
            count[nums[r]]+=1
            while l<r and  count[nums[r]]>1:
                s-=nums[l]
                count[nums[l]]-=1
                l+=1
            ans=max(ans,s)
        return ans
            

        