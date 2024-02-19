
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        count = 0
        out = 0
        result = 0

        while r < len(nums):
            if nums[r] % 2 != 0:
                count += 1

            while count == k:
                right_count = 1
                while r + 1 < len(nums) and nums[r + 1] % 2 == 0:
                    r += 1
                    right_count += 1

                left_count = 1
                while nums[l] % 2 == 0:
                    left_count += 1
                    l += 1

                out += left_count * right_count

                if nums[l] % 2 != 0:
                    count -= 1

                l += 1

            r += 1

        return out
