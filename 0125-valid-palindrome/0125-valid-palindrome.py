class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char.lower()for char in s if char.isalnum())
        p = s[::-1]
        if s == p:
            return True
        else:
            return False 