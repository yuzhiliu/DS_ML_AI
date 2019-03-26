import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        n = len(s)
        count = collections.Counter(t)
        start = 0
        nt = len(t)
        min_len = float('inf')
        while r < n:
            if count[s[r]] > 0:
                nt -= 1
            count[s[r]] -= 1
            r += 1
            while nt == 0:
                if r - l < min_len:
                    min_len = r - l
                    start = l
                count[s[l]] += 1
                if count[s[l]] > 0:
                    nt += 1
                l += 1
        return s[start:start + min_len] if start + min_len <= len(s) else ''
