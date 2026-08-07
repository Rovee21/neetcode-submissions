class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #go through every combination and have max val
        #[10,1,5,6,7,1]
        retVal = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                val = prices[j] - prices[i]
                retVal = max(retVal, val)

        return retVal