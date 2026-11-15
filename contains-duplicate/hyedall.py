"""
https://leetcode.com/problems/contains-duplicate/

시간 복잡도: O(n)
- set 변환 O(n)

공간 복잡도: O(n)
- set에 저장
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
