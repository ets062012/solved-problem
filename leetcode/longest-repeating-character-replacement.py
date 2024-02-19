class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        max_repeat = 0
        char_count = [0] * 26  

        while r < len(s):
            char_count[ord(s[r]) - ord('A')] += 1
            max_repeat = max(max_repeat, char_count[ord(s[r]) - ord('A')])

            while (r - l + 1 - max_repeat) > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
