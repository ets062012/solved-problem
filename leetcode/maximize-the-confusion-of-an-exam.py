class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = i = 0
        char_count = Counter()

        for j, char in enumerate(answerKey):
            char_count[char] += 1
            max_freq = max(max_freq, char_count[char])

            if j - i + 1 > max_freq + k:
                char_count[answerKey[i]] -= 1
                i += 1

        return len(answerKey) - i
