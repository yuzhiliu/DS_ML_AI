class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat:
            return 0
        res = 0
        m, n = len(mat), len(mat[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + mat[i-1][j-1]
                l, r = 1, min(i, j)
                while l <= r:
                    m = l + (r - l) // 2
                    cur_sum = dp[i][j] - dp[i-m][j] - dp[i][j-m] + dp[i-m][j-m]
                    if cur_sum <= threshold:
                        l = m  + 1
                        res = max(res, m)
                    else:
                        r = m - 1
        return res

    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat:
            return 0
        res = 0
        m, n = len(mat), len(mat[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + mat[i-1][j-1]
                 m = res + 1
                 if i >= m and j >= m and threshold >= dp[i][j] - dp[i-m][j] - dp[i][j-m] + dp[i-m][j-m]:
                     res = m
        return res
