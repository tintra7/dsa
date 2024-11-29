from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        path = [[0] * n for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                path[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0] != 1:
                path[j][0] = 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))