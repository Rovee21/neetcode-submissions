class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = 0
        buy = 1
        while(buy<len(prices)):
            if(prices[buy]<prices[sell]):
                sell=buy
            profit = max(profit,prices[buy]-prices[sell])
            buy+=1
        return profit