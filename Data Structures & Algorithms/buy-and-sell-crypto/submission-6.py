class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l=5, r=5 , retVal = 6
        #[10,1,5,6,7,1]
        
        retVal = 0
        l,r= 0,1
        while(r<len(prices)):
            retVal = max(retVal, (prices[r]-prices[l]))
            if(prices[r]<prices[l]):
                l = r
            r += 1
        
        return retVal


        