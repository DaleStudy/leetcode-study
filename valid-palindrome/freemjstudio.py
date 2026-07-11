class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()

        filtered = ""
        for ch in s:
            if ch in characters:
                filtered += ch

        n = len(filtered)
        left = 0
        right = n-1
        while left <= n//2 and right >= n//2:
            if filtered[left] == filtered[right]:
                left += 1
                right -= 1
            else:
                return False

        return True