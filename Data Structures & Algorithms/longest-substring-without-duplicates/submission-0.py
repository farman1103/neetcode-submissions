class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        for i in range(len(s)):
            ss = set()
            for j in range(i, len(s)):
                if s[j] not in ss:
                    ss.add(s[j])
                    maxl = max(maxl, len(ss))
                elif s[j] in ss:
                    break
        return maxl