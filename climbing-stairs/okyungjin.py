# 시간 복잡도: O(N)
# 공간 복잡도: O(1)

# [요구사항]
# 1. 계단의 개수 n이 주어진다.
# 2. 계단은 1칸 또는 2칸 올라갈 수 있다.
# 3. 마지막 칸에 도달할 수 있는 경우의 수를 반환한다.

# [접근법]
# 1. 계단에 올라올 수 있는 경우의 수는 전전칸까지의 경우의 수 (prev2) + 전칸까지의 경우의 수 (prev1) 를 더한 값이다.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1 # 전전칸 까지의 경우의 수
        prev1 = 2 # 전칸 까지의 경우의 수

        for _ in range(2, n):
            curr = prev2 + prev1 # 현재 계단
            prev2 = prev1
            prev1 = curr

        return prev1
