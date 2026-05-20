"""
# Approach
nums 집합을 만들어 없는 숫자를 찾습니다.

# Complexity
- Time complexity: nums 의 길이를 n이라고 할 때, O(n)
- Space complexity: O(n)
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_set = set(nums)
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums_set:
                return i
