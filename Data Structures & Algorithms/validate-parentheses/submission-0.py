class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hs = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in hs:
                if stack and stack[-1] == hs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False