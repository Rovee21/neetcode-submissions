class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input: XYYX -> count how many of the same chars we can get in a row -> 4
        #edge cases: len(s)>0, k<len(s), k can be 0
        #optimal solution: 
        #"AAABABB" k = 1
        #res = 5, l= 0, r = 5, freqMap = {A: 4, B:2}

        def getMaxFreq(hm):
            maxVal = 0
            for vals in hm.values():
                maxVal = max(maxVal,vals)

            return maxVal

        freqMap = {}
        l,r=0,0
        res = 0
        while(r<len(s)):
            print(res)
            freqMap[s[r]] = 1 + freqMap.get(s[r],0)
            r +=1
            if((r-l)- getMaxFreq(freqMap)<=k):
                res = max(res,r-l)
            else:
                freqMap[s[l]] = freqMap.get(s[l]) - 1
                l+=1

        return res




        