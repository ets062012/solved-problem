class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        result = []
        
        for word in words:
            w = set(word.lower())
            if w.issubset(s1) or w.issubset(s2) or w.issubset(s3):
                result.append(word)
        return result


        