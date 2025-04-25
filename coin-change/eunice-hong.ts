
/**
 * 
 * Time Complexity: O(n * amount)
 * Space Complexity: O(amount)
 */
function coinChange(coins: number[], amount: number): number {
  // Initialize dp array with Infinity
  const dp = new Array(amount + 1).fill(Infinity);
  // Base case: 0 coins needed to make amount 0
  dp[0] = 0;

  // Iterate through each coin
  for (let coin of coins) {
    // Update dp array for each amount from coin to amount
    for (let i = coin; i <= amount; i++) {
      // Choose the minimum between current dp[i] and dp[i - coin] + 1
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  // If dp[amount] is still Infinity, it means it's not possible to make the amount
  return dp[amount] === Infinity ? -1 : dp[amount];
}