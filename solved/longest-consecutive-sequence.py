class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_consec = 0

        for num in num_set:
            if num - 1 not in num_set:  
                current_num = num
                current_consec = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_consec += 1

                longest_consec= max(longest_consec , current_consec)

        return longest_consec 
        