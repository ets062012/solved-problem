class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        ans = 0
        mod = 10**9 + 7
        
        for ins in instructions:
            index1 = bisect_left(nums, ins)
            left = index1
            index2 = bisect_right(nums, ins)
            right = len(nums) - index2
            ans += min(left, right)
            ans %= mod
            nums.insert(index1, ins)
        
        return ans
