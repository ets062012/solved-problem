class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            arr.append(s)

            
        return arr

