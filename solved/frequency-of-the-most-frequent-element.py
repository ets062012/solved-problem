class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,maxx = 0, 1
        runsum = nums[0]
        for right in range(1, len(nums)):
            runsum += nums[right]
            curr = (1+right-left) * nums[right]
            if runsum + k >= curr:
                maxx = max(maxx, right - left + 1)
            else:
                while left<right and runsum + k < curr:
                    runsum -= nums[left]
                    curr -= nums[right]
                    left += 1
                maxx = max(maxx, right - left +1)
        return maxx

        