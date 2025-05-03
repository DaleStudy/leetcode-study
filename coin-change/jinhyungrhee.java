import java.util.*;
class Solution {
    int INF = 987654321;
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, INF);

        dp[0] = 0;
        for (int coin : coins) {
            if (coin <= amount) dp[coin] = 1;
        }

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if ((i - coin) >= 0) dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return (dp[amount] == INF) ? -1 : dp[amount];
    }
}
