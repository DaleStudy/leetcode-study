"""
n = nums의 길이
시간 복잡도: O(n) - 시작점에서만 세어 나가서 각 숫자는 최대 두 번만 확인
공간 복잡도: O(n) - 모든 숫자를 담는 set
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 수열의 시작점에서만 길이를 센다
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
