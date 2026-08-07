class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = ""
        right = ""
        l = 0
        r = len(s) -1

        while(l<r or len(right)!=len(left)):
            if(len(left)<=len(right)):
                if(s[l].isalnum()):
                    left += s[l]
                l+=1
            if(len(right)<len(left)):
                if(s[r].isalnum()):
                    right += s[r]
                r-=1
        
        print(left)
        print(right)
        return left.lower()==right.lower()
