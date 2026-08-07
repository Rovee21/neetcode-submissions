class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use hashmaps and compare hashmaps at the end

        shm = {}
        for c in s:
            shm[c] = 1 + shm.get(c,0)
        
        thm = {}
        for c in t:
            thm[c] = 1 + thm.get(c,0)

        return thm == shm