"""
Solution

Algorithm:
    1. Create a set from the list.
    2. If the length of the set is not equal to the length of the list, return True.
    3. Otherwise, return False.

Time complexity: O(n)
Space complexity: O(n)
"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def main():
    test_cases = [
        [
            [1, 2, 3, 1],
            True,
        ][[1, 2, 3, 4], False],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
    ]
    s = Solution()

    for test_case in test_cases:
        nums_input, expected = test_case
        assert s.containsDuplicate(nums_input) == expected


if __name__ == "__main__":
    main()
