class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num%3:
            return []
        n=num//3
        sumi=n+n-1+n+1
        if sumi==num:
            return[n-1,n,n+1]
