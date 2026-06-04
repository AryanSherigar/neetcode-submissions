class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minB = prices[0]

        for sell in prices:
            ans = max(ans, sell-minB)
            minB = min(minB, sell)
        
        return ans
        