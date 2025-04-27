class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        end = len(filtered) - 1
        if end <= 0:
            return True
        start = 0
        while True:
            end_s = filtered[end]
            start_s = filtered[start]
            if end_s == start_s:
                end -= 1
                start += 1


            else:
                return False
            if start >= end:
                return True
            if end <= 0:
                return True
            continue


