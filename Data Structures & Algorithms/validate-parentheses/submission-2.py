class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack and if it is an open bracket add it if it is a closed bracket iterate until open bracket and if not same then return false
        stack = []
        hm = {')' : '(', '}':'{', ']':'['}

        #)(
        
        for c in s:
            if c in hm:
                if stack and stack[-1]==hm[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
            
        



