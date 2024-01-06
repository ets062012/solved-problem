class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros_prefix = [0] * (n + 1)
        ones_suffix = [0] * (n + 1)

        for i in range(n):
            zeros_prefix[i + 1] = zeros_prefix[i] + (nums[i] == 0)

        for i in range(n - 1, -1, -1):
            ones_suffix[i] = ones_suffix[i + 1] + (nums[i] == 1)

        max_score = float('-inf')
        max_score_indices = []

        for i in range(n + 1):
            score = zeros_prefix[i] + ones_suffix[i]

            if score > max_score:
                max_score = score
                max_score_indices = [i]
            elif score == max_score:
                max_score_indices.append(i)

        return max_score_indices