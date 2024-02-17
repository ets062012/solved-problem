class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1

        last_index = {}
        max_distance = float('inf')

        for i, card in enumerate(cards):
            if card in last_index:
                max_distance = min(max_distance, i - last_index[card])
            last_index[card] = i

        return max_distance + 1 if max_distance != float('inf') else -1