class Solution(object):
    # https://www.cnblogs.com/grandyang/p/10828725.html
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j - 1])
        return dp[0][-1] > 0

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = piles[:]
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                dp[i] = max(piles[i] - dp[i+1], piles[j] - dp[i])
        return dp[0] > 0

    def stoneGame(self, piles):
	return True


    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for j in range(n)] for i in range(n)]
        def dfs(i, j):
            if i == j:
                return piles[i]
            if dp[i][j] == 0:
                dp[i][j] = max(piles[i] - dfs(i + 1, j), piles[j] -  dfs(i, j - 1))
            return dp[i][j]
                
        return dfs(0, len(piles) - 1)
