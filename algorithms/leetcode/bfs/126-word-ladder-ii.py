class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        # BFS
        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word in endWord:
                    res.extend(layer[word])
                else:
                    for i in range(len(word)):
                        for c in string.ascii_lowercase:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in wordList:
                                new_layer[new_word] += [w + [new_word] for w in layer[word]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return res
