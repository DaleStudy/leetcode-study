'''
시간 복잡도: O(n^2)
- 각 인덱스 `i`에서 최대 `nums[i]` 범위만큼의 `step`을 탐색하며, 최악의 경우 O(n)번의 내부 연산이 수행됩니다.

공간 복잡도: O(n)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        dp = [False] * n
        dp[-2] = (nums[-2] >= 1)

        for i in range(n - 3, -1, -1):
            num = nums[i]
            can_jump_to_end = (num >= n - i - 1)
            if can_jump_to_end:
                dp[i] = True
                continue
            
            can_jump_through_next_index = any([dp[i + step] for step in range(1, min(num + 1, n))])
            dp[i] = can_jump_through_next_index

        return dp[0]


'''
시간 복잡도: O(n)
- 배열을 한 번만 순회하면서 가장 멀리 도달할 수 있는 위치를 갱신하므로 O(n)입니다.

공간 복잡도: O(1)
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i > max_reach:  # 현재 인덱스가 도달 가능한 최대 범위를 넘어선 경우
                return False
            
            max_reach = max(max_reach, i + nums[i])  # 도달 가능한 최대 거리 갱신
            
            if max_reach >= n - 1:  # 마지막 인덱스에 도달 가능하면 True 반환
                return True
        
        return False
