class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s=0
        count=0
        remainderdic=defaultdict(int)
        remainderdic[0]=1
        for num in nums:
            s+=num
            if s%k  in remainderdic:
                count+=remainderdic[s%k]
            remainderdic[s%k]+=1
        return count



        
        