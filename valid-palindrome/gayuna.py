class Solution(object):
    # Time complexity: O(n)

    # Iterate through all characters, check for alphabet and number. trimmed string should only contain lower case letters and numbers.
    # use two pointer. one from head and one from tail. iterate all char to the inside.
    # early return if two characters are different. if loop ends, it's palindrome.
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        trimmed = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                trimmed += c.lower()
        
        for i in range(len(trimmed)//2):
            if trimmed[i] != trimmed[-(1+i)]:
                return False
        return True