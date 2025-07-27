from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        q = deque()
        q.append((beginWord, 1))  

        while q:
            word, level = q.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord == endWord:
                        return level + 1
                    if newWord in wordSet:
                        q.append((newWord, level + 1))
                        wordSet.remove(newWord)
        return 0
