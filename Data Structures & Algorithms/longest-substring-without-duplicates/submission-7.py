class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Solution: use a set to see if there is duplicates and keep sliding window

        #zxyzxyz
        #set={z,x,}, res=2, l=0, r=1
        charSet = set()
        l = 0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res



        




        



