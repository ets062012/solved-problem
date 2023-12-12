class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxim=max(candies)
        res=[]
        s=0
        for i in range(len(candies)):
            s=candies[i]+extraCandies
            if s>=maxim:
                res.append(True)
            else:
                res.append(False)
        return res

        