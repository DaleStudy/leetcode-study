/* 
Time Complexity: O(coins.length * amount)
Space Complexity: O(amount)

1 ~ i-1원까지의 최적해를 알고 있다면, i원의 최적해를 구할 때 coins 배열 iteration으로 구할 수 있음
*/
class Solution {
    public int coinChange(int[] coins, int amount) {
        int c = coins.length;

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, 99999);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < c; j++) {
                if (i - coins[j] < 0) {
                    continue;
                }
                if (dp[i - coins[j]] >= 0 && dp[i - coins[j]] + 1 < dp[i]) {
                    dp[i] = dp[i - coins[j]] + 1;
                }
            }
        }

        return dp[amount] == 99999 ? -1 : dp[amount];
    }
}
