class Solution {
  int coinChange(List<int> coins, int amount) {
    List<int> dp = List.filled(amount + 1, amount + 1);
    // S(n) = O(amount)
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        // T(n) = O(amount * coins.length)
        dp[i] = 1 + coins.where((x) => x <= i)
                .map((x) => dp[i - x])
                .fold(amount, (a, b) => min(a, b));
    }
    return dp[amount] <= amount ? dp[amount] : -1;
  }
}
