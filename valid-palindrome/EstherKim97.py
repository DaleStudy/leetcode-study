class Solution(object):
    def isPalindrome(self, s):
        import re
        # remove all non-alphanumeric characters
        s = re.sub(r'\W+', '', s.lower())

        # check if the string is equal forward and backward
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
