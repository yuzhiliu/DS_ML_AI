class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        n = len(s)
        count = {}
        res = 0
        while l <= r and r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            while len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

if __name__ == '__main__':
    s = 'eceba'
    k = 2
    print Solution().lengthOfLongestSubstringKDistinct(s, k)
