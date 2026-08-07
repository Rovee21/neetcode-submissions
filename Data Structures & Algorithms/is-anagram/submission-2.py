class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        numS, numT = {},{}

        for n in range(len(s)):
            numS[s[n]] = 1 + numS.get(s[n],0)
            numT[t[n]] = 1 + numT.get(t[n],0)

        return numS==numT
         

        