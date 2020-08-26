class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if dp[i - j**2] == 0:
                    dp[i] = True
                    break
        return dp[n]

    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.dfs(n, {})
    
    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n == 1
        res = False
        for i in range(1, int(n**0.5) + 1):
            if self.dfs(n - i**2, memo) == False:
                res = True
                break
        memo[n] = res
        return res
