class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        main_sum = sum(mat[i][i] for i in range(n))
        secondary_sum = sum(mat[i][n - i - 1] for i in range(n))
        if n % 2 == 1:
            mid = n // 2
            return main_sum + secondary_sum - mat[mid][mid]
        else:
            return main_sum + secondary_sum


