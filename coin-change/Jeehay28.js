/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

// TC : O(c*a), where c is the number of coins, and a is amount
// SC : O(a) // dp array requires O(a) space

var coinChange = function (coins, amount) {
  // dynamic programming approach

  // dp[amount] : the minimum number of coins
  // as a default, dp[0] = 0, for other amounts, dp[amount] = amount + 1 ()
  // [0, amount+1, amount+1, ...]
  const dp = [0, ...new Array(amount).fill(amount + 1)];

  // start from coin because i - coin >= 0
  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      // dp[i] : not using the current coin
      // dp[i - coin] + 1 : using the current coin
      dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
    }
  }

  // dp[amount] === amount + 1 : that amount of money cannot be made up by any combination of the coins
  return dp[amount] < amount + 1 ? dp[amount] : -1;
};


