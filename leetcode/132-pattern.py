class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        
        z=-float('inf')
        flag=False
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=z:
                while stack and nums[i]>stack[-1]:
                    a=stack.pop()
        
                    z=a
                stack.append(nums[i])
                
            else:
                return True
        print(stack)
        return False
       

        