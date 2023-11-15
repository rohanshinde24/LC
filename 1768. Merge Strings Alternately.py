class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        l1 = len(word1)
        l2 = len(word2)
        for i in range(0,min(l1,l2)):
            new += word1[i]
            new += word2[i]
        new += word1[i+1:]
        new += word2[i+1:]
        return new