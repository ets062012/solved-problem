class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)-1):
            arr.append(sum(nums[:i+1]))
            
        arr.append(sum(nums))
        return arr

