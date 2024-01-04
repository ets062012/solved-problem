class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target=0
        output=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue;
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=a+nums[l]+nums[r]
                if sum<target:
                    l+=1

                elif sum>target:
                    r-=1
                else:
                    output.append([nums[i],nums[r],nums[l]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return output




                

                

        

