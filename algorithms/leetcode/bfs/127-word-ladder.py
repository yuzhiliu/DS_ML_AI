import string
import collections
class Solution(object):
    # two sided BFS
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord)
        wordList.discard(endWord)
        while front:
            # generate all valid transformations
            newFront = set()
            for phrase in front:
                for i in range(len(beginWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = phrase[:i] + c + phrase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordList:
                            newFront.add(nw)
                            #wordList.discard(nw)
                            wordList.remove(nw)
            front = newFront
            # swap front and back for better performance (fewer choices in
            # generating nextSet)
            if len(front) > len(back):
                front, back = back, front
            # remove transformations from wordList to avoid cycle
            wordList -= front
            length += 1
        return 0


    # BFS + queue
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        queue.append((next_word, length + 1))
                        wordList.remove(next_word)
        return 0
