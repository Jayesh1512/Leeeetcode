class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = 'a'
        while(len(word) < k):
            for i in word:
                word += chr(ord(i) + 1)
        return word[k-1]