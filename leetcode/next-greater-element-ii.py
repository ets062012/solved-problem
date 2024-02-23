class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[(0,nums[0])]
        arr=[]
        res=[-1]*(2*len(nums))
        for i in range(2*len(nums)):
            arr.append(nums[i%len(nums)])
        for i,c in enumerate(arr):
            while stack and c>stack[-1][1]:
                a=stack.pop()
                res[a[0]]=c
            stack.append((i,c))

        return res[:len(nums)]


        