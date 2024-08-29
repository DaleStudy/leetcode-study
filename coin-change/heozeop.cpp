// Time Complexity: O(n * amount)
// Spatial Complexity: O(amount)

const int MAX_VALUE = 10001;
const int IMPOSSIBLE = -1;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        vector<int> dp(amount + 1, MAX_VALUE);

        dp[0] = 0;
        for(int i = 0; i <= amount; ++i) {
            for(int coin : coins) {
                if (i < coin) {
                    continue;
                }

                dp[i] = min(1 + dp[i - coin], dp[i]);
            }
        }

        if (dp[amount] == MAX_VALUE) {
            return IMPOSSIBLE;
        }

        return dp[amount];
    }
};
