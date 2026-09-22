class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = prices[0]
        j = 0
        for x in prices:
            i = min(i,x)
            j = max(j, x-i)
        return j
            