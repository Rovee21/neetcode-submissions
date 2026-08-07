class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort and compare
        return sorted(s)==sorted(t)