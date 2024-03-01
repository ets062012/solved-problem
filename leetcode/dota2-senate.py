class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        r=deque()
        d=deque()
        for i in range(len(senate)):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)
        print(r)
        print(d)
        while r and d:
            rturn=r.popleft()
            dturn=d.popleft()
            if rturn<dturn:
                r.append(dturn+len(senate))
            else:
                d.append(rturn+len(senate))
        return "Radiant" if r else "Dire"
        