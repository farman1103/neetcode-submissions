class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ipmap = { '[':']', '{':'}', '(':')' }
        for ch in s:
            if ch in ipmap:
                stack.append(ch)
            elif stack and ipmap[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return not stack