class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if not strs:
            return ""
        i=0
        while i< len(strs[0]):
            char= strs[0][i]
            for s in strs[1:]:
                if s[i]!= char or i== len(s):
                    return strs[0][:i]
            i+=1
        return strs[0]
        
            
        