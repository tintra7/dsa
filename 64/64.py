from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        path_sum = [[0] * n for i in range(m)]
        path_sum[0][0]= grid[0][0]
        for i in range(1, n):
            path_sum[0][i] = path_sum[0][i-1] + grid[0][i]
        for i in range(1, m):
            path_sum[i][0] = path_sum[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                path_sum[i][j] = min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]
        return path_sum[-1][-1]

s = Solution()
print(s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))