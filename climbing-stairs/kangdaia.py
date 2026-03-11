class Solution:
    def climbStairs(self, n: int) -> int:
        """
        한번에 1계단 혹은 2계단 씩 올라갈 수 있을때, n개의 계단을 올라기가 위한 방법의 수를 구하는 함수

        방법:
        1. dp로 풀이하기. 점화식 계산
            n=2일때, 1,1 / 2 -> 2가지
            n=3일때, 1,1,1 / 1,2 / 2,1 -> 3가지
            n=4일때, 1,1,1,1 / 1,1,2 / 1,2,1 / 2,1,1 / 2,2 -> 5가지
             1) n-1에서 1계단 올라가기
             2) n-2에서 2계단 올라가기
            -> dp[i] = dp[i-1] + dp[i-2]
        2. 이전 값 두개만 알아두면 되니, dp 배열을 만들지 않고, prev1, prev2로 계산하기
        시간복잡도 O(n), 공간복잡도 O(1)

        Args:
            n (int): 최종적으로 올라가야 하는 계단의 수

        Returns:
            int: n개의 계단을 올라가기 위한 방법의 갯수
        """
        if n <= 3:
            return n
        prev1, prev2 = 2, 3
        for i in range(3, n):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2