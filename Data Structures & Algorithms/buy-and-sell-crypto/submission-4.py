class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l=0, r=1
        #maxProf = 0
        #prices = [10,8,7,5,2]

        #if prices[r]-prices[l]>0 then increase right, if not l=r
        l, r = 0,1
        maxProfit = 0
        while r < len(prices):
            if prices[r]-prices[l]<=0:
                l = r
            maxProfit = max(maxProfit, prices[r]-prices[l])
            r+=1
        
        return maxProfit


