class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        op = ""
        while (len(op) != (len(word1) + len(word2))):
            if len(word1) > l :
                op += word1[l]
                l += 1
            if len(word2) > r :
                op += word2[r]
                r +=1
        return op