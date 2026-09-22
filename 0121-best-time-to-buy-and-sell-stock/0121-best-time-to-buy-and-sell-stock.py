class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = prices[0]
        diff = 0
        for j in range(1, len(prices)):
            sub = prices[j] - i
            diff = max(diff, sub)
            i = min(i, prices[j])
        return diff