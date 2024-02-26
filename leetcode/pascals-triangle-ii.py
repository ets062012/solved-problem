class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            target=[0]*(len(res)+1)
            for j in range(len(res)):
                target[j]+=res[j]
                target[j+1]+=res[j]
            res=target
        return res
        