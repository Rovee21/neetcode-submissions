class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxc = 0
        right = 0
        for i in range(len(s)):
            right = i
            while right<len(s) and (s[right] not in chars):
                chars.add(s[right])
                right+=1
            maxc=max(right-i,maxc)
            chars.clear()           
        return maxc