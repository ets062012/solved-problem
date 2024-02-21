class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pair={")":"(","}":"{","]":"["}
        for c in s:
            if c in pair:
                if stack and stack[-1]==pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0





            
        
