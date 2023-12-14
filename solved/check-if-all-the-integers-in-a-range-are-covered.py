class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s=set()
        for a,b in ranges:
            current_range = range(a,b+1)
            s.update(current_range)
        lr= set(range(left,right+1))
        return lr<=s
        