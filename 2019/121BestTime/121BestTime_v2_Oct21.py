class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #FIXED check empty array
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_v = prices[0]
        for i in range(1, len(prices)) :
            if prices[i] < min_v:
                min_v = prices[i]
            elif prices[i] - min_v > max_profit:
                max_profit = prices[i] - min_v
        
        return max_profit
        
        
