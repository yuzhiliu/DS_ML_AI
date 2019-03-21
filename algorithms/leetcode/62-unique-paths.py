class Solution(object):
    # DFS TLE
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.dfs(m, n, 0, 0)

    def dfs(self, m, n, i, j):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        return self.dfs(m, n, i + 1, j) + self.dfs(m, n, i, j + 1)


    # DFS + memo
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.dfs2(m, n, 0, 0, {})

    def dfs2(self, m, n, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        memo[(i, j)] = self.dfs2(m, n, i + 1, j, memo) + self.dfs2(m, n, i, j + 1, memo)
        return memo[(i, j)]


    # 2D DP
    def uniquePaths3(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]
        return dp[m-1][n-1]

    # 1D DP
    def uniquePaths4(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] += dp[j-1]
        return dp[n-1]


if __name__ == '__main__':
    m = 4
    n = 3
    print Solution().uniquePaths(m, n)
    print Solution().uniquePaths2(m, n)
    print Solution().uniquePaths3(m, n)
    print Solution().uniquePaths4(m, n)
