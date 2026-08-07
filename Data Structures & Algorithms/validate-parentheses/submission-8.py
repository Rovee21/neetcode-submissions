class Solution:
    def isValid(self, s: str) -> bool:
        #Input: s = "([{}])"
        #stack = [], parenthesis = {"}":"{", "]":"[", ")":"("}

        parenthesis = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if(c=='{' or c=='[' or c=='('):
                stack.append(c)
            else:
                if(not stack or parenthesis[c]!=stack[-1]):
                    return False
                stack.pop()
        
        if stack:
            return False
        return True