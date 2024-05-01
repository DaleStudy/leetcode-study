class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = [i for i in s.lower() if i.isalnum()]
        return ans == ans[::-1]

        # TC: O(n)
        # SC: O(n)
