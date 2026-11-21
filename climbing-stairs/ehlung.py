"""
n = 계단 수
시간 복잡도: O(n) - 2층부터 n층까지 한 번씩 계산
공간 복잡도: O(1) - 배열 없이 변수 두 개만 사용
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # n층에 오는 방법 = (n-1)층에서 한 칸 + (n-2)층에서 두 칸
        prev2, prev1 = 1, 1  # 0층, 1층에 오는 방법 수
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1
