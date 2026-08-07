class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #"pwwkew"
        #dup= {p,w}, res=2, l=1 , r=2
        l, r =0,0
        dup = set()
        res = 0
        while r<len(s):
            while s[r] in dup:
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            res = max(r-l+1,res)
            r+=1
        return res

        
            
