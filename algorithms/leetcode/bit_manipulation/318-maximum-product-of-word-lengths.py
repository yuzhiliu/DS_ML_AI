class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= (1 << ord(c) - ord('a'))
            dic[mask] = max(dic.get(mask, 0), len(w))

        res = 0
        for x in dic:
            for y in dic:
                if not x & y:
                    res = max(res, dic[x] * dic[y])
        return res
