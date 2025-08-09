class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = "".join(elem.lower() for elem in s if elem.isalnum())

        # sol 1
        # Time complexity: O(n)
        return formatted_string == formatted_string[::-1]

        # sol 2
        # Time complexity: O(n)
        left = 0
        right = len(formatted_string) - 1
        while left < right:
            if formatted_string[left] != formatted_string[right]:
                return False
        left += 1
        right -= 1
        return True
