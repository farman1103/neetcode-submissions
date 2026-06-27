class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(1,len(prices)):
            j = i-1
            if prices[i] > prices[j]:
                profits.append(prices[i] - prices[j])
        return sum(profits)