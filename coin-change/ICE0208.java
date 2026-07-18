class Solution {
    /**
     * 시간 복잡도: O(amount * coins.length)
     * 공간 복잡도: O(amount)
     */
    public int coinChange(int[] coins, int amount) {
        // 필요한 동전의 최대 개수는 amount개이므로,
        // amount + 1은 만들 수 없는 상태를 나타내기에 충분하다.
        int impossible = amount + 1;

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, impossible);
        dp[0] = 0;

        for (int currentAmount = 1; currentAmount <= amount; currentAmount++) {
            for (int coin : coins) {
                if (coin > currentAmount) {
                    continue;
                }

                dp[currentAmount] = Math.min(
                    dp[currentAmount],
                    dp[currentAmount - coin] + 1
                );
            }
        }

        return dp[amount] == impossible ? -1 : dp[amount];
    }
}
