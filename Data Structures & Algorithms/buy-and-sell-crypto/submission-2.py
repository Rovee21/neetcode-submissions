class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #O(n^2) compare every element, and store the highest difference in a var
        profit = 0
        for i in range(len(prices)):
            j = i+1
            while(j<len(prices)):
                if(prices[j]-prices[i]>profit):
                    profit=prices[j]-prices[i]
                j+=1
        return profit
            

