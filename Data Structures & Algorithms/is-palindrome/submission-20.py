class Solution:
    def isPalindrome(self, s: str) -> bool:
        #get the string remove all of the spaces and reverse it and compare
        # update=""
        # for c in s:
        #     if c.isalnum():
        #         update += c.lower()
        
        # if update == update[::-1]:
        #     return True
        # else:
        #     return False


        #two pointers
        #tab a cat
        l,r = 0,len(s)-1
        while(l<r):
            while not s[l].isalnum() and l<r:
                l+=1
            while not s[r].isalnum() and l<r:
                r-=1
            if (s[l].lower()!= s[r].lower()):
                return False
            l+=1
            r-=1
        return True