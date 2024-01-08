class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        arr = [0] * len(flips)
        c = 0
        max_index = 0
        ones_count = 0

        for i in range(len(arr)):
            arr[flips[i] - 1] = 1
            max_index = max(max_index, flips[i])
            ones_count += 1
            if (i == 0 or ones_count == max_index) and sum(arr[i+1:]) == 0:
                c += 1

        return c
        