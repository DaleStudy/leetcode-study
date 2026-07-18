import java.util.*;

// TC: O(n * amount)  (n = coins.length)
// SC: O(amount)
class Solution {

    private static final int IMPOSSIBLE = Integer.MAX_VALUE;

    private int[] memo;

    public int coinChange(int[] coins, int amount) {
        memo = new int[amount + 1];
        Arrays.fill(memo, -1);

        int result = minCoins(amount, coins);
        return result == IMPOSSIBLE ? -1 : result;
    }

    private int minCoins(int target, int[] coins) {
        if (target == 0) return 0;
        if (target < 0) return IMPOSSIBLE;
        if (memo[target] != -1) return memo[target];

        int best = IMPOSSIBLE;
        for (int coin : coins) {
            int sub = minCoins(target - coin, coins);
            if (sub != IMPOSSIBLE) {
                best = Math.min(best, sub + 1);
            }
        }
        return memo[target] = best;
    }
}
