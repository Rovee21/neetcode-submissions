class Solution:
    def isPalindrome(self, s: str) -> bool:
        #get the string remove all of the spaces and reverse it and compare
        update=""
        for c in s:
            if c.isalnum():
                update += c.lower()
        
        if update == update[::-1]:
            return True
        else:
            return False