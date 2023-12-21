class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        replacement_list = {}
        for op1, op2 in reversed(operations):
                replacement_list[op1] = replacement_list.get(op2, op2)

        
        for i, val in enumerate(nums):
            if val in replacement_list:
                nums[i]=replacement_list[val]
                      

        return nums
        
        