class Solution {

    private int answer = Integer.MAX_VALUE;

    public int coinChange(int[] coins, int amount) {
        final int IMPOSSIBLE = amount + 1;

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, IMPOSSIBLE);
        dp[0] = 0;

        for (int i = 1; i < amount + 1; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] == IMPOSSIBLE ? -1 : dp[amount];
    }
}