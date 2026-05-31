from typing import List

"""
Ideation:
    배열을 정렬한 뒤, 인접한 숫자들을 비교하면서 가장 긴 연속 수열의 길이를 구한다.
    
    - 같은 숫자는 중복이므로 건너뛴다.
    - 현재 숫자 + 1 이 다음 숫자와 같으면 연속된 수이므로 길이를 증가시킨다.
    - 연속이 끊기면 최대 길이를 갱신하고 길이를 1로 초기화한다.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 0
        length = 1

        nums.sort()

        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                continue
            if nums[idx] + 1 == nums[idx + 1]:
                length += 1
            else:
                longest = max(longest, length)
                length = 1
        longest = max(longest, length)
        return longest
