class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q=deque()
        q.append(deck[len(deck)-1])
        if len(deck)<=2:
            return deck
        else:
            for i in range(len(deck)-2,-1,-1):
                q.appendleft(deck[i])
                a=q.pop()
                q.appendleft(a)
            a=q.popleft()
            q.append(a)
        return q


        