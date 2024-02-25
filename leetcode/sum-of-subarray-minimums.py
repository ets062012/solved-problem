class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        MOD=10**9+7
        res=0
        for i,n in enumerate(arr):
            while stack and n<stack[-1][1]:
                ind,value=stack.pop()
                left=ind-stack[-1][0] if stack else ind+1
                right=i-ind
                res=(res+value*left*right)%MOD
            stack.append((i,n))
        for i in range(len(stack)):
            ind,value=stack[i]
            left=ind-stack[i-1][0] if i>0 else ind+1
            right=len(arr)-ind

            res=(res+value*left*right)%MOD


        return res
        