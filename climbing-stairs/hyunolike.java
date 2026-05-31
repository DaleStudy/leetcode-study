class Solution {
    public int climbStairs(int n) {
        
        // 경우의 수 하기 >> 피보나치?
        // ways(n) = ways(n-1) + ways(n-2)

        if(n == 1) return 1;
        if(n == 2) return 2;

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
}
