class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s = "OUZ OD YXAZ V", t = "XYZ"
        #haveHM={z: 1, y:1, x:1}, needHM={x:1,y:1, z:1}, have = 3, need = 3, l=6, r=8
        #res = [6,9], 2

        needHM, haveHM = {},{}
        for c in t:
            needHM[c] = needHM.get(c, 0) + 1
        need, have = len(needHM), 0
        l=0
        res, reslen = [-1,-1], float("infinity")

        for r in range(len(s)):
            haveHM[s[r]] = haveHM.get(s[r],0)+1
            if s[r] in needHM and haveHM[s[r]]==needHM[s[r]]:
                have += 1
            while need == have:
                if((r-l) < reslen):
                    reslen = r-l
                    res = [l, r+1]

                haveHM[s[l]] -= 1
                if(s[l] in needHM and haveHM[s[l]]<needHM[s[l]]):
                    have -= 1
                l+=1
        
        if reslen == "infinity":
            return ""
        else:
            l, r = res
            return s[l:r]

                


