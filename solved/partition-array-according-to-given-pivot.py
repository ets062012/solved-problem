class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result=[]
        pivotHigh=[x for x in nums if x>pivot]
        pivotLow=[x for x in nums if x<pivot]
        pivotBet=[x for x in nums if x==pivot]
        
      
        for i in range(len(pivotLow)):
            result.append(pivotLow[i])
        for i in range(len(pivotBet)):
            result.append(pivotBet[i])
        for i in range(len(pivotHigh)):
            result.append(pivotHigh[i])
        return result







        