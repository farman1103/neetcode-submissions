class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for i in range(1,len(prices)):
            j = i-1
            if prices[i] > prices[j]:
                profits += (prices[i] - prices[j])
        return profits