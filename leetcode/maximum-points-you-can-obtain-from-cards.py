class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        r=len(cardPoints)-k
        s=sum(cardPoints[r:])
        res=s
        while r<len(cardPoints):
            s+=(cardPoints[l]-cardPoints[r])
            res=max(res,s)
            l+=1
            r+=1
        return res


        