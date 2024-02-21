class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if i==")" and "(" in stack:
                stack.remove("(")
            else:
                stack.append(i)
        return len(stack)
        