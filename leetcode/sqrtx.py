class Solution:
    def mySqrt(self, x: int) -> int:
        target=sqrt(x)
        low=0
        high=x
        while low<=high:
            mid=(high+low)//2
            if mid<target:
                low=mid+1
            elif mid>target:
                high=mid-1

            else:
                return mid
        return min(low,high)
        