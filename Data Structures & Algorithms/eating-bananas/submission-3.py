class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l<=r:
            m = (l+r)//2
            tHours = 0
            for p in piles:
                tHours += math.ceil(p/m)
            
            if(tHours<=h):
                k = min(m,k)
                r = m-1
            else:
                l = m+1
        return k