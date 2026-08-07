class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force would be to go through and look through each element in s and make sure
        #it is in t and remove both


        #sort and compare strings

        return sorted(s)==sorted(t)