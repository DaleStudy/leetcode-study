class Solution {
    public int climbStairs(int n) {
        /*
         * i번째 계단에 도착하는 경우는 두 가지다.
         *
         * 1. i - 1번째 계단에서 한 칸 올라오는 경우
         * 2. i - 2번째 계단에서 두 칸 올라오는 경우
         *
         * dp[i]를 i번째 계단에 도착하는 방법의 수라고 하면,
         * dp[i] = dp[i - 1] + dp[i - 2] 이다. (i >= 3)
         *
         * 이때 dp[i]를 구하기 위해 필요한 값은 직전 값과 전전 값뿐이다.
         * 따라서 dp 배열 전체를 만들지 않고 prev1, prev2 두 변수만 사용해 갱신한다.
         *
         * 시간 복잡도: O(n)
         * 공간 복잡도: O(1)
         */

        if (n <= 2) {
            // 1번째 계단은 1가지, 2번째 계단은 2가지 방법으로 오를 수 있다.
            return n;
        }

        int prev2 = 1; // dp[1]
        int prev1 = 2; // dp[2]

        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2; // dp[i]
            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
}
