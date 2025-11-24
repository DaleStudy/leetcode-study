class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^0-9A-Za-z]', '',s).lower()
        return s == s[::-1]
        