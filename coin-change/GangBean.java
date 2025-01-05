class Solution {
    public int coinChange(int[] coins, int amount) {
        /**
        1. understanding
        - given coins that can be used, find the minimum count of coins sum up to input amount value.
        - [1,2,5]: 11
            - 2 * 5 + 1 * 1: 3 -> use high value coin as much as possible if the remain can be sumed up by remain coins.
        2. strategy
        - If you search in greedy way, it will takes over O(min(amount/coin) ^ N), given N is the length of coins.
        - Let dp[k] is the number of coins which are sum up to amount k, in a given coin set.
        - Then, dp[k] = min(dp[k], dp[k-coin] + 1)
        3. complexity
        - time: O(CA), where C is the length of coins, A is amount value
        - space: O(A), where A is amount value
        */

        int[] dp = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            dp[i] = amount + 1;
        }

        for (int coin: coins) { // O(C)
            for (int k = coin; k <= amount; k++) { // O(A)
                dp[k] = Math.min(dp[k], dp[k-coin] + 1);
            }
        }

        return (dp[amount] >= amount + 1) ? -1 : dp[amount];
    }
}

