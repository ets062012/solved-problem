class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        return str(int(''.join(nums)))
        