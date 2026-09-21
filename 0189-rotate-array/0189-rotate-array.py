class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j= len(nums)-1
        k = k % len(nums)
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums