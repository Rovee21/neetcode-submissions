class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combos = {"}":"{" , ")":"(", "]":"["}
        for c in s:
            if c in combos and stack:
                if combos[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack