class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l , r = 0, 0
        n = len(s)
        count = collections.Counter()
        while l <= r and r < n:
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

if __name__ == '__main__':
    s = 'abcabcd'
    print Solution().lengthOfLongestSubstring(s)
