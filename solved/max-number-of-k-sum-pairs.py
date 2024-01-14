class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = {}
        for num in nums:
            complement = k - num
            if complement in num_count and num_count[complement] > 0:
                count += 1
                num_count[complement] -= 1
            else:
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1
        return count
        