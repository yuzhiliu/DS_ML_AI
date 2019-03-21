class Solution(object):
    # DFS + memo
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        return self.dfs(obstacleGrid, m, n, 0, 0, {})

    def dfs(self, grid, m, n, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if i + 1 < m and grid[i+1][j] != 1:
            r = self.dfs(grid, m, n, i + 1, j, memo)
        else:
            r = 0
        if j + 1 < n and grid[i][j+1] != 1:
            d = self.dfs(grid, m, n, i, j + 1, memo)
        else:
            d = 0
        memo[(i, j)] = r + d
        return memo[(i, j)]

    # 2D DP
    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]

    # 1D DP
    def uniquePathsWithObstacles3(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if j > 0:
                        dp[j] += dp[j-1]
                else:
                    dp[j] = 0
        return dp[n-1]


if __name__ == '__main__':
    obstacleGrid = [
          [0,0,0],
          [0,0,0],
          [1,0,0],
          [0,0,0]]
    print Solution().uniquePathsWithObstacles(obstacleGrid)
    print Solution().uniquePathsWithObstacles2(obstacleGrid)
    print Solution().uniquePathsWithObstacles3(obstacleGrid)
