class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        splitter=path.split("/")
        for i in splitter:
            if i=="" or i==".":
                continue
            elif i=="..":
                if  stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        return "/"+"/".join(stack)