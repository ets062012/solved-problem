class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i=="./":
                pass
            elif i=="../" and stack:
                stack.pop()
            elif i!="../" and i!= "./":
                stack.append(i)
       
        return len(stack)