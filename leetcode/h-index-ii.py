class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1  
        n = high  
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= (n - mid + 1):
                high = mid - 1
            else:
                low = mid + 1
        return n - low + 1
