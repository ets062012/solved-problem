class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCapacity(mid):
            
            count = 0
            for pile in piles:
               count+=ceil(pile/mid)
                
            return count <= h

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            if isCapacity(mid):
                high = mid-1    
            else:
                low = mid + 1
        return low
        