// n: amount m: length of coins
// Time complexity: O(n * m) + O(mlogm)
// Space complexity: O(n)

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = Array.from({ length: amount + 1 }, () => Infinity);
  dp[0] = 0;

  coins.sort((a, b) => a - b);

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp.at(-1) === Infinity ? -1 : dp.at(-1);
};
