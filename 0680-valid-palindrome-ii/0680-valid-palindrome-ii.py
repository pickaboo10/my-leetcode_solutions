class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                left = i+1
                right = j
                skipleft = True
                while(left<right):
                    if s[left]!= s[right]:
                        skipleft = False
                        break
                    left+=1
                    right-=1
                left = i
                right = j-1
                skipright = True
                while(left<right):
                    if s[left]!= s[right]:
                        skipright = False
                    left+=1
                    right-=1
                return skipleft or skipright
        return True