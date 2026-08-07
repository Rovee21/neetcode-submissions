class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #"AAABABB", k = 1
        #hm={A: 1, B:2}, l = 3, r = 5, retVal = 5

        hm = {}
        retVal = 0
        l,r = 0,0
        while r<len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            r += 1
            print("l = " + str(l))
            print("r = " + str(r))
            print((r-l)-max(hm.values()))
            if(((r-l)-max(hm.values()))<=k):
                retVal = max(retVal,(r-l))
            else:
                print("goes in here")
                while(((r-l)-max(hm.values()))>k):
                    hm[s[l]] = hm.get(s[l], 0) - 1
                    l+=1

        return retVal