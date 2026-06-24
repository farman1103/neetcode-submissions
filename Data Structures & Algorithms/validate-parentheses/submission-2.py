class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p = '(,{,['
        for ch in s:
            if ch in open_p:
                stack.append(ch)
            else:
                if stack:
                    poped = stack.pop()
                    if poped == '(' and ch == ')':
                        continue
                    if poped == '{' and ch == '}':
                        continue
                    if poped == '[' and ch == ']':
                        continue
                    return False
                else:
                    return False
        if stack:
            return False
        else:
            return True