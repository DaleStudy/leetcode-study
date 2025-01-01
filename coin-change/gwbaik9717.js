// n: amount m: length of coins
// Time complexity: O(n * m) + O(mlogm)
// Space complexity: O(n * m)

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = Array.from({ length: coins.length + 1 }, () =>
    Array.from({ length: amount + 1 }, () => Infinity)
  );
  coins.sort((a, b) => a - b);

  for (let i = 0; i < coins.length + 1; i++) {
    dp[i][0] = 0;
  }

  for (let i = 1; i <= amount; i++) {
    for (let j = 1; j <= coins.length; j++) {
      const coin = coins[j - 1];

      if (i >= coin) {
        dp[j][i] = Math.min(dp[j][i], 1 + dp[j][i - coin]);
      }

      dp[j][i] = Math.min(dp[j][i], dp[j - 1][i]);
    }
  }

  return dp.at(-1).at(-1) === Infinity ? -1 : dp.at(-1).at(-1);
};
