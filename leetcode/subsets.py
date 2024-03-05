class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack (first_num, path):
            if len(path)==len(nums):
                return
           
            for i in range(first_num,len(nums)):
                path.append(nums[i])
                ans.append(path[:])
                backtrack(i+1,path)
                path.pop()
            return
        ans=[]
        backtrack(0,[])
        ans.append([])
        return ans
        