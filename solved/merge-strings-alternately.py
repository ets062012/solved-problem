class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        one = len(word1)
        two = len(word2)
        smallest = min((len(word1), len(word2)))
        MergeResponse = ''

        for letter in range(smallest):
            MergeResponse  += word1[letter]
            MergeResponse += word2[letter]

        if one < two:
            MergeResponse  += word2[one:]

        else:
            MergeResponse  += word1[two:]

        return MergeResponse
