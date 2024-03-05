class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        def backtrack(first_num, path):
            if sum(path) == n and len(path)==k:
                ans.append(path[:])
                return

            for i in range(first_num, len(nums)):
                if i > first_num and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates

                if sum(path) + nums[i] > n:
                    break  # Prune unnecessary branches

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        ans = []
        
        backtrack(0, [])

        return ans

        