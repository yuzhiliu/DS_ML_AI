class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            pali = self.helper(s, i, i)
            if len(pali) > len(res):
                res = pali
            pali = self.helper(s, i, i + 1)
            if len(pali) > len(res):
                res = pali
        return res
    
    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        res = s[0]
        n = len(s)
        max_len = 1
        dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                res = s[i:i+2]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        res = s[i:j+1]
        return res 

    # Manacher
