class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        types=Counter(answers)
        res=0
        for key,value in types.items():
            if key==0:
                res+=value
            elif key!=0 and value<key+1:
                res+=key+1
            else:
                res+=(key+1)*(ceil(value/(key+1)))
        return res
        