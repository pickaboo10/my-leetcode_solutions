class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = 0
        min_len = len(nums)+1
        total = 0
        for high in range(len(nums)):
            total+= nums[high]
            while total>= target:
                min_len = min(min_len, high-low+1)
                total-=nums[low]
                low+=1
        if min_len == len(nums)+1:
            return 0
        return min_len