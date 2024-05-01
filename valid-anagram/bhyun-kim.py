"""
Solution

Algorithm:
    1. Sort the strings and compare them.
    2. If they are equal, return True. Otherwise, return False.

Time complexity: O(nlogn)
Space complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if sorted(s) == sorted(t):
            return True
        else:
            return False


def main():
    test_cases = [
        ["anagram", "nagaram", True],
        ["rat", "car", False]
    ]
    s = Solution()
    
    for test_case in test_cases:
        s_input, t_input, expected = test_case
        assert s.isAnagram(s_input, t_input) == expected

if __name__ == '__main__':
    main()