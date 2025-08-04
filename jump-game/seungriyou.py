# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
    def canJump_slow_dp(self, nums: List[int]) -> bool:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n)

        [Approach]
            dp[i] = i-th idx에서 마지막 칸까지 도달 가능한지 여부
            맨 오른쪽 칸까지의 도달 가능 여부를 확인해야 하므로, nums[i] 만큼 오른쪽으로 가봐야 한다.
            따라서 맨 오른쪽부터 dp table을 채워나가면 되고, nums[i] 만큼 오른쪽으로 가보다가 True일 때가 나오면 빠르게 break 한다.
        """
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        # i 보다 오른쪽 값이 필요하므로, 오른쪽에서부터 dp table 채워나가기
        for i in range(n - 2, -1, -1):
            # i에서 nums[i] 만큼 오른쪽으로 가보기
            for di in range(nums[i] + 1):
                # 중간에 마지막 칸까지 도달 가능한 칸이 나온다면, dp[i] = True & break
                if dp[i + di]:
                    dp[i] = True
                    break

        return dp[0]

    def canJump_greedy(self, nums: List[int]) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            왼쪽 idx부터 확인하며, 특정 idx에서 오른쪽 방향으로 최대한 갈 수 있는 max_step을 greedy 하게 트래킹한다.
            이때, 다음 idx로 넘어갈 때마다 최대한 갈 수 있는 max_step에서 -1을 해주어야 하며,
            중간에 max_step이 음수가 되는 경우라면 마지막 idx까지 진행할 수 없는 것이므로 False를 반환한다.
        """
        max_step = 0

        for n in nums:
            # max_step이 음수가 되는 경우라면, 마지막 idx까지 진행할 수 없음
            if max_step < 0:
                return False

            # max_step 업데이트
            if max_step < n:
                max_step = n

            # 다음 idx로 넘어가기 위해 max_step--
            max_step -= 1

        return True

    def canJump(self, nums: List[int]) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            맨 오른쪽 idx에 도달할 수 있는 idx(= idx_can_reach_end)를 트래킹함으로써 DP 풀이를 optimize 할 수 있다.
            nums의 오른쪽 원소부터 확인하면서, i + nums[i]가 idx_can_reach_end 보다 gte 이면
            **idx_can_reach_end를 거쳐서 맨 오른쪽 idx에 도달할 수 있는 것**이므로 idx_can_reach_end를 i로 업데이트 한다.
            모든 순회가 끝나고, idx_can_reach_end == 0인지 여부를 반환하면 된다.
        """
        n = len(nums)
        # 맨 오른쪽 idx에 도달할 수 있는 idx
        idx_can_reach_end = n - 1

        # 오른쪽에서부터 확인
        for i in range(n - 2, -1, -1):
            # 현재 idx에서 idx_can_reach_end를 거쳐서 맨 오른쪽 idx에 도달할 수 있는 경우, idx_can_reach_end 업데이트
            if i + nums[i] >= idx_can_reach_end:
                idx_can_reach_end = i

        return idx_can_reach_end == 0
