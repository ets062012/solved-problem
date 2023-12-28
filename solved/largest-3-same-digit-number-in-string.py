class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            if len(set(num[i:i+3])) == 1:
                if num[i:i+3] > max_good:
                    max_good = num[i:i+3]
        return max_good