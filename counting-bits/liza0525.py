# 7기 풀이
# 시간 복잡도: O(n)
# - n의 크기만큼 모든 수에 대한 dp 값을 찾음
# 공간 복잡도: O(n)
# - n의 크기만큼 dp 어레이를 사용
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]

        return dp
