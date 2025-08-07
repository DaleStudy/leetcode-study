//Dynamic Programming
//dp[n] = dp[n-1]+dp[n-2]
class Solution {
public:
    int climbStairs(int n) {
        int dp[46];
        
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;

        for(int i=3; i<=n; i++)
        {
            dp[i] = dp[i-1]+dp[i-2];
        }

        return dp[n];

    }
};
