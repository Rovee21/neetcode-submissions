class Solution:
    def isPalindrome(self, s: str) -> bool:
        #go through the string and add all alnum characters to string and see if the string reads the same way backwards
        #Input: s = "Was it a car or a cat I saw?"
        #alnumS=""
        
        # alnumS = ""
        # for c in s:
        #     if(c.isalnum()):
        #         alnumS += c.lower()

        # return alnumS==alnumS[::-1]


        #two pointers l, r, if alnum() compare the .lower() values and if they dont match then return false
        #"tab a cat" ,l=0, r=8

        l, r = 0, len(s)-1

        while(l<r):
            while(l<r and not s[l].isalnum()):
                l += 1
            while(l<r and not s[r].isalnum()):
                r -= 1
            if(s[l].lower()!=s[r].lower()):
                return False
            l+=1
            r-=1
        return True
