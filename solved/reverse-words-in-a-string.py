class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        
        reversed_string = ' '.join(reversed(words))

        return reversed_string

        