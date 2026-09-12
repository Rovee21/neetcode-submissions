class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #pwwkew
        #l=1, r = 4, len = 3, dup = {a,b,c}
        l = 0
        r = 0
        dup = set()
        retlen = 0
        while r<len(s):
            while s[r] in dup:
                dup.remove(s[l])
                l+=1
            else:
                dup.add(s[r])
                r +=1
                retlen = max(retlen, (r-l))
        
        return retlen
