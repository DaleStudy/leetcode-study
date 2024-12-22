// dp문제
// i번째 계단을 가려면 i-1번째 계단까지의 경우의 수와 i-2번째 계단까지의 경우의 수를 합친 것
// 시간복잡도 : O(N)
// 공간복잡도 : O(N)
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2;i<n+1;i++){
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[n];

    }
}
