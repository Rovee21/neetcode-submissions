class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while(l<r):
            if not self.is_alnum(s[l].lower()):
                l+=1
            elif not (self.is_alnum(s[r].lower())):
                r-=1
            elif (s[l].lower()!=s[r].lower()):
                return False
            else:
                l+=1
                r-=1
        return True


    def is_alnum(self, s):
        if((48<=ord(s) and ord(s)<=57) or (97<=ord(s) and ord(s)<=122)):
            return True
        return False
