class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        words1res=""
        words2res=""
        for i in range(len(word1)):
            words1res+=word1[i]
        for i in range(len(word2)):
            words2res+=word2[i]
        return words1res==words2res
