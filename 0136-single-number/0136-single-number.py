class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for key,value in hash.items():
            if value==1:
                return key