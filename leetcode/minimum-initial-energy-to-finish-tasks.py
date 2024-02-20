class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        task = sorted(tasks, key=lambda x: (x[1] - x[0], x[1]), reverse=True)
        curr_min = 0
        ans = 0
        
        for actual, minimum in task:
            if curr_min < minimum:
                ans += minimum - curr_min
                curr_min = minimum 
               
            curr_min -= actual
        
        return ans
