class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(first_num, path):
            if sum(path) == target:
                ans.append(path[:])
                return

            for i in range(first_num, len(candidates)):
                if i > first_num and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates

                if sum(path) + candidates[i] > target:
                    break  # Prune unnecessary branches

                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        ans = []
        candidates.sort()
        backtrack(0, [])

        return ans
