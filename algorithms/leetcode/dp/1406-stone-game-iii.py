class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 3)
        cnt = 0
        for i in range(n - 1, -1, -1):
            cnt += stoneValue[i]
            dp[i] = cnt - min(dp[i+1:i+4])
        return 'Tie' if cnt - dp[0] == dp[0] else 'Alice' if cnt - dp[0] < dp[0] else 'Bob'
