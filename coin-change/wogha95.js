// TC: O(C * A)
// SC: O(C)
// C: coins.length, A: amount

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(Number.MAX_SAFE_INTEGER);
  dp[0] = 0;

  for (let index = 1; index < amount + 1; index++) {
    for (const coin of coins) {
      if (index - coin >= 0) {
        dp[index] = Math.min(dp[index - coin] + 1, dp[index]);
      }
    }
  }

  return dp[amount] === Number.MAX_SAFE_INTEGER ? -1 : dp[amount];
};
