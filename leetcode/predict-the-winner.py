from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}  
        
        def helper(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            pickLeft = nums[left] - helper(left + 1, right)
            pickRight = nums[right] - helper(left, right - 1)
            
            memo[(left, right)] = max(pickLeft, pickRight)
            
            return memo[(left, right)]
        
        return helper(0, len(nums) - 1) >= 0
