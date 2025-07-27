
"""
[문제]
https://leetcode.com/problems/contains-duplicate/description/

[문제 접근 방법]
Set 자료구조를 활용하여 중복 여부를 개수로 확인한다.

[Complexity]
N: nums 길이
TC: O(N)
SC: O(N)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

