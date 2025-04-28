/**
 * 시간 복잡도: O(amount * coins.length)
 * 각 금액에 대해 모든 동전을 고려해야 함
 */

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);

  dp[0] = 0; // 금액 0은 동전이 필요 없음

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      // dp[i] : 금액 i를 만들기 위한 최소 동전 개수
      // dp[i - coin] + 1 : 현재 동전을 한 개 사용하고 나머지 금액(i - coin)을 만드는 최소 동전 개수
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
};
