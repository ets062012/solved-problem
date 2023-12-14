class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4
        for num in arr:
            if arr.count(num) > threshold:
                return num
        