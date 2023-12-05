class Solution(object):
    def interpret(self, command):
        newstr = ''
        for i in range(len(command)-1):
            if command[i] == "(" and command[i+1] == ")":
                newstr+="o"
            else:
                newstr+=command[i]
        newstr+=command[-1]
        s = ''
        for i in newstr:
            if i == "(":
                s+=""
            else:
                s+=i.replace(")", "")
        return s


        