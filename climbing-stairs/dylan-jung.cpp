class Solution {
int dp[45] = { 0 };
public:
    int climbStairs(int n) {
        dp[0] = 1;
        if(n > 1) dp[1] = 2;
        for(int i = 2; i < n; i++)
            dp[i] = dp[i-1] + dp[i-2];
        return dp[n-1];
    }
};
