class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # pointer for next valid position
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # keep this element
                k += 1
        return k