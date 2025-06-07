"""
https://leetcode.com/problems/jump-game/description/

문제: 배열 nums가 주어질 때, 각 인덱스에서 최대 점프 거리를 나타내는 배열이다.
    배열의 마지막 인덱스에 도달할 수 있으면 true, 아니면 false를 반환해라.

풀이: 
    1. 현재 인덱스에서 최대 점프 거리를 계산한다.
    2. 최대 점프 거리가 배열의 마지막 인덱스를 넘으면 true, 아니면 false를 반환한다.

TC: O(n), SC: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0  # 현재까지 도달 가능한 최대 인덱스
        for idx in range(len(nums)): # 각 위치 순회
            if idx <= reach:  # 현재 인덱스가 도달 가능한 최대 인덱스 이하면
                reach = max(reach, idx + nums[idx])  # 최대 점프 거리 갱신
        return len(nums) - 1 <= reach  # 마지막 인덱스가 도달 가능한 최대 인덱스 이상이면 true
