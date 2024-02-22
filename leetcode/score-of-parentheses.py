class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        stack.append(0)
        for c in s:
            if c=="(":
                stack.append(0)
            elif c==")":
                a=stack.pop()
                stack[-1]+=max(a*2,a+1)
        return stack[0]
       

        