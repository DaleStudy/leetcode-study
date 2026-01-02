class Solution {
public:
    long dp[10001];
    int coinChange(vector<int>& coins, int amount) {
        long INF = (long)1 << 31;
        fill(dp, dp+10001, INF);

        for(int& item: coins) {
            if(item > 10000) continue;
            dp[item] = 1;
        }

        for(int i = 1; i <= amount; i++) {
            for(int& item: coins) {
                int j = i - item;
                if(j > 0 && dp[j] != -1) {
                    dp[i] = min(dp[j] + 1, dp[i]);
                }
            }
        }

        if(dp[amount] == INF) {
            if(amount == 0) return 0;
            else return -1;
        }
        return dp[amount];
    }
};
