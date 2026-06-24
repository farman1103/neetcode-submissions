class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt ={}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        for i in range(len(t)):
            if t[i] in countt:
                countt[t[i]] += 1
            else:
                countt[t[i]] = 1

        if countt == counts:
            return True
        else:
            return False