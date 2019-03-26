class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l, r = 0, 0
        n = len(s)
        count = {}
        while l <= r and r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            while len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

if __name__ == '__main__':
    s = "ecebba"
    print Solution().lengthOfLongestSubstringTwoDistinct(s)
