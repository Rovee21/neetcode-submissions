class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = s.replace(" ", "")
        newStr = newStr.lower()
        l, r = 0, len(newStr)-1
        while(l<r):

            while not(newStr[l].isalnum()) and l<r:
                l+=1
            while not(newStr[r].isalnum()) and l<r:
                print(r)
                r-=1
            if(newStr[l]!=newStr[r]):
                return False
            if(l<r):
                l +=1
                r -=1
        return True