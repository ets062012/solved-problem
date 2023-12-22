class Solution:
    
    def totalMoney(self, n: int) -> int:
        ans = 0
        current_week = n // 7

        for i in range(current_week):
            ans += 28 + (i * 7)

        remaining_days = n % 7

        for day in range(1, remaining_days + 1):
            ans += current_week + day

        return ans


        