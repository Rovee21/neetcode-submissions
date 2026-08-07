class Solution:
    def isValid(self, s: str) -> bool:
        #([{}])
        #create a stack and pop when closed bracket and brackets match
        #stack = [(, ]
        stack = []
        bHashmap = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in bHashmap.values():
                stack.append(c)
            elif (c in bHashmap) and stack and stack[-1]==bHashmap.get(c):
                stack.pop()
            else:
                return False
        
        return not stack


