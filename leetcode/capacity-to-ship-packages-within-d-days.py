class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isCapacity(mid):
            s = 0
            count = 1
            for weight in weights:
                if s + weight > mid:
                    count += 1
                    s = weight
                else:
                    s += weight
            return count <= days

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if isCapacity(mid):
                high = mid-1    
            else:
                low = mid + 1
        return low


