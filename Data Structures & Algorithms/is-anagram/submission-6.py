class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force would be to go through and look through each element in s and make sure
        #it is in t and remove both


        #sort and compare strings
        # return sorted(s)==sorted(t)

        #hashmap, have the value as the key and the number of accurances as the value
        if(len(s)!=len(t)):
            return False

        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
