"""
Solution:

Algorithm: 
    1. Convert the string to lowercase.
    2. Remove all non-alphanumeric characters.
    3. Check if the string is equal to its reverse.

Time complexity: O(n)
Space complexity: O(n) 
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalpha() or c.isnumeric()]
        return s == s[::-1]


def main():
    test_cases = [
        ["A man, a plan, a canal: Panama", True],
        ["race a car", False],
        [" ", True],
    ]
    s = Solution()

    for test_case in test_cases:
        s_input, expected = test_case
        assert s.isPalindrome(s_input) == expected


if __name__ == "__main__":
    main()
