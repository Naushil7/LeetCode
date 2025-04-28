class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # prev[j] = number of paths to reach cell (i-1, j)
        prev = [1] * n  # First row: only one way to reach any cell (only right moves)

        for i in range(1, m):
            curr = [1] * n  # First column: always one way (only down moves)
            for j in range(1, n):
                curr[j] = curr[j-1] + prev[j]  # left + up
            prev = curr  # Move to next row

        return prev[n-1]