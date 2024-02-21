class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters=Counter(s)
        res=0
        odd=0
        for key,value in letters.items():
            if value>1:
                if value%2==0:
                    res+=value
                else:
                    res+=value-1
                    odd+=1
            else:
                odd+=1
        if odd>0:
            res+=1
        return res                

        