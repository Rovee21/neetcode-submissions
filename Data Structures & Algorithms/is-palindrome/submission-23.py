class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force
        #tab a cat #tabacat
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        
        return newS==newS[::-1]