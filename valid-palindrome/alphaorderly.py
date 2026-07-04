"""
Time Complexity: O(N)
Space Complexity: O(N)

- Process string with lower() and isalnum() to remove non-alphanumeric characters
- Check if the processed string is a palindrome by comparing it to its reverse
"""
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         processed = "".join(ch.lower() for ch in s if ch.isalnum())

#         return processed == processed[::-1]

"""
Time Complexity: O(N)
Space Complexity: O(1)

- Use two pointers to check if the string is a palindrome
- Skip non-alphanumeric characters
- Compare characters from both ends towards the center
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)

        left, right = 0, N - 1

        while True:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if left >= right:
                break

            if s[left].lower() == s[right].lower():
                left, right = left + 1, right - 1
            else:
                return False

        return True
