class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dvdf
        #dup={v}, retVal = 2, l =1, r=2
        dup = set()
        retVal = 0
        l, r = 0,0
        while(r<len(s)):
            if s[r] not in dup:
                dup.add(s[r])
                r+=1
                retVal = max(retVal, (r-l))
            else:
                while s[r] in dup:
                    dup.remove(s[l])
                    l+=1

        return retVal