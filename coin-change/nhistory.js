/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  for (let i = 0; i <= amount; i++) {
    for (const coin of coins) {
      if (coin <= i) dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
    }
  }

  return dp[amount] < amount + 1 ? dp[amount] : -1;
};

// TC: O(amount*coins.length)
// SC: O(amount)
