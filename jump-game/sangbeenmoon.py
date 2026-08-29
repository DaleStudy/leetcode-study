# 탑다운
# 재귀 깊이가 n 까지 깊어질 수 있어서 비효율적.

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # memo[i] = i 번째에서 도달할 수 있는 최대 인덱스.
        memo = [0] * len(nums)

        def go(cur : int) -> int:
            if cur >= len(nums) - 1:
                return -1
            if memo[cur] != 0:
                return memo[cur]

            max_jump = nums[cur]

            if max_jump == 0:
                return cur


            for jump in range(max_jump,0,-1):
                res = go(cur + jump)
                if res == -1:
                    return -1
                memo[cur] = max(memo[cur], res)

            return memo[cur]

        return True if go(0) == -1 else False

# 바텀업

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n              # dp[i] = i에서 마지막까지 갈 수 있는가
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            max_reach = min(i + nums[i], n - 1)
            for j in range(i + 1, max_reach + 1):
                if dp[j]:
                    dp[i] = True
                    break             # 하나만 찾으면 충분
            # 못 찾으면 dp[i]는 초기값 False 그대로

        return dp[0]
