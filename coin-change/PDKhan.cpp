class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            vector<int> dp(amount+1, amount+1);
    
            dp[0] = 0;
            
            for(int i = 1; i <= amount; i++){
                for(int j = 0; j < coins.size(); j++){
                    if(i >= coins[j])
                        dp[i] = min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
    
            if(dp[amount] > amount)
                return -1;
    
            return dp[amount];
        }
    };
