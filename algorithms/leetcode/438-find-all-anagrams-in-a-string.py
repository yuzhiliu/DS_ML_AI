import collections
class Solution(object):
    def findAnagrams0(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        ns, np = len(s), len(p)
        res = []
        pcount = collections.Counter(p)
        scount = collections.Counter(s[:np-1])
        r = np-1
        while r < ns:
            scount[s[r]] += 1
            if scount == pcount:
                res.append(r - np + 1)
            scount[s[r-np+1]] -= 1

            if scount[s[r-np+1]] == 0:
                del scount[s[r-np+1]]
            r += 1
        return res
                if c in dic:
                    if dic[c] >= 0:
                        count += 1
                    dic[c] += 1
                l += 1
            r += 1
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print Solution().findAnagrams(s, p)
