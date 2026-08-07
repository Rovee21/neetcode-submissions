class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxc = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            maxc=max((r-l)+1,maxc)           
        return maxc