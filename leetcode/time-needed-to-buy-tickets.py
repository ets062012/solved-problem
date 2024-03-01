class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        indexarr=[i for i in range(len(tickets))]
        q=deque(indexarr)
        time=0
        while q:
            for i in range(len(q)):
                idx=q.popleft()
                if tickets[idx]>0:
                    tickets[idx]-=1
                    time+=1
                if tickets[k]==0:
                    return time
                if tickets[idx]>0:
                    q.append(idx)
        