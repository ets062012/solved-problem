class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        counts = [0] * (max_cost + 1)

        for cost in costs:
            counts[cost] += 1

        bars_bought = 0
        for i in range(len(counts)):
            while counts[i] > 0 and coins >= i:
                coins -= i
                counts[i] -= 1
                bars_bought += 1

        return bars_bought
        