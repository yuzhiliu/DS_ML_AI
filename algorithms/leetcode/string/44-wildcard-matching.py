class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns, np = len(s), len(p)
        dp = [[False for j in range(np + 1)] for i in range(ns + 1)]
        for i in range(ns + 1):
            for j in range(np + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = p[j - 1] == '*' and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = False
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    # for k in range(i+1):
                    #     if dp[k][j - 1] == True:
                    #         dp[i][j] = True
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]
