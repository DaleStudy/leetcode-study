class Solution {
public:
int coinChange(vector<int>& coins, int amount) {
int MAX = 10000 + 1;
vector<int> memo(amount + 1, MAX);
memo[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (auto coin : coins) {
                if (i - coin >= 0) {
                    memo[i] = min(memo[i], memo[i - coin] + 1);
                }
            }
        }

        return memo[amount] == MAX ? -1 : memo[amount];
    }

};
