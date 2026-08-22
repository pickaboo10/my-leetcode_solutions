class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        high = 0 
        freq ={}
        max_len = 0
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0)+1
            while freq[s[high]]>1:
                freq[s[low]]-=1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low+=1
            max_len = max(max_len , high-low+1)
        return max_len


