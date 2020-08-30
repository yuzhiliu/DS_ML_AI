class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns, np = len(s) + 1, len(p) + 1
        dp = [[False for j in range(np)] for i in range(ns)]
        dp[0][0] = True
        for j in range(2, np):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, ns):
            for j in range(1, np):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2] # not use the character before *
                    if s[i-1] == p[j-2] or  p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                elif p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] & (s[i-1] == p[j-1])
        return dp[-1][-1]
                    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return first_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        return first_match and self.isMatch(s[1:], p[1:])
