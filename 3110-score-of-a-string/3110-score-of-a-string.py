class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        add = 0
        for i in range(len(s)-1):
            x = abs(ord(s[i+1])- ord(s[i]))
            add+=x
        return add

        