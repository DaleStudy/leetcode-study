"""
n = nums의 길이
시간 복잡도: O(n) - 각 집을 한 번씩 확인
공간 복잡도: O(1) - 배열 없이 변수 두 개만 사용
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        # prev2: 두 집 전까지의 최대 금액, prev1: 바로 전 집까지의 최대 금액
        prev2, prev1 = 0, 0
        for money in nums:
            prev2, prev1 = prev1, max(prev2 + money, prev1)
        return prev1
