class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sets = set()
        res = set()
        for i in range(len(s) - 9):
            subs = s[i:i+10]
            #print(i, subs)
            if subs in sets:
                res.add(subs)
            else:
                sets.add(subs)
        return list(res)
