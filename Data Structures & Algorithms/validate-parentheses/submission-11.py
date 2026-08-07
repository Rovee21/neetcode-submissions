class Solution:
    def isValid(self, s: str) -> bool:
        #([{}]), stack = (,[,{
        stack = deque()
        par ={"}" : "{","]" : "[", ")" : "("}

        for c in s:
            if c=='(' or c =='{' or c == '[':
                stack.append(c)
            else:
                if(stack and stack[-1]==par[c]):
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
