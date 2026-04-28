class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= len(nums)/2
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
            if freq[x]>a:
             return x
        