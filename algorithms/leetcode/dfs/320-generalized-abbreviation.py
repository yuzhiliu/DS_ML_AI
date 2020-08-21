class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        idx = 0
        path = ''
        count = 0
        self.dfs(word, idx, path, count, res)
        return res
    
    def dfs(self, word, idx, path, count, res):
        if idx == len(word):
            res.append(path + str(count) if count > 0 else path)
            return

        self.dfs(word, idx + 1, path, count + 1, res)
        self.dfs(word, idx + 1, path + (str(count) if count else '') + word[idx], 0, res )
