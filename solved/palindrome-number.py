class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        newstr=str(x)
        return newstr==newstr[::-1]
        