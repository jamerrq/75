class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        r = ""
        while i < len(word1) and j < len(word2):
            r += word1[i]
            r += word2[j]
            i += 1
            j += 1
        r += word1[i:]
        r += word2[j:]
        return r
