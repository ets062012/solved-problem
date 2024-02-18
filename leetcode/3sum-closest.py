class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
    
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
        
            while start < end:
                current_sum = nums[i] + nums[start] + nums[end]
            
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
            
                if current_sum > target:
                    end -= 1
                else:
                    start += 1

        return closest_sum
    