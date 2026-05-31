/**
 * Runtime: 0ms
 * Time Complexity: O(n)
 *
 * Memory: 42.18MB
 * Space Complexity: O(n)
 *
 * Approach: DP를 이용한 점화식 활용
 * - n번째 계단에 도달하는 방법은 (n-1)번째 계단에서 한 칸 올라오는 방법과
 *                          (n-2)번째 계단에서 두 칸 올라오는 방법의 합과 같음
 */
class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        else if (n == 2) return 2;

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i=3; i<dp.length; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
}
