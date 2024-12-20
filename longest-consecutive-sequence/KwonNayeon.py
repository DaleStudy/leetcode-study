"""
Title: 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Question:
    - Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    - You must write an algorithm that runs in O(n) time.

Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9

Time Complexity:
    - O(n log n)
Space Complexity:
    - O(n)

Notes:
    - sorted(nums)를 사용하면 TC가 O(n log n)이 되어 문제의 조건을 충족하지 못하지만, 이 방법이 제가 생각해서 풀 수 있는 최선이라 일단 이대로 제출합니다! 다른 분들 답안 참고하여 다시 풀어보겠습니다 :)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_length = 0
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        max_length = max(max_length, current_length)
        return max_length
