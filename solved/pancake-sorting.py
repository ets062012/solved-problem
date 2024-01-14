from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        for x in range(n, 1, -1):
            idx = arr.index(x)
            if idx != x - 1:
                if idx != 0:
                    arr = arr[:idx+1][::-1] + arr[idx+1:]
                    result.append(idx + 1)
                arr = arr[:x][::-1] + arr[x:]
                result.append(x)
        return result
