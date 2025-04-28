/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  // dp[i]는 금액 i를 만들기 위한 최소 코인 수
  const dp = new Array(amount + 1).fill(Infinity);

  // 금액 0을 만들기 위해 필요한 코인 수는 0개
  dp[0] = 0;

  // 1부터 amount까지 반복
  for (let i = 1; i <= amount; i++) {
    // 각 금액마다 모든 코인 시도
    for (let coin of coins) {
      if (i - coin >= 0) {
        // 코인을 하나 사용했을 때, 남은 금액의 최소 개수 + 1
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  // 만약 Infinity면 만들 수 없는 금액임
  return dp[amount] === Infinity ? -1 : dp[amount];
};
