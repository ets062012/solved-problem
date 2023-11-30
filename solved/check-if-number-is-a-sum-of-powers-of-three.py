class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            n,ans=divmod(n,3)
            if ans==2:
                return False
        return True