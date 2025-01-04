// 시간 복잡도: O(n * m)
// 공간 복잡도: O(n)

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (let coin of coins) {
      for (let i = coin; i <= amount; i++) {
          dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
};

