/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  // f(n) = n을 만드는데 필요한 동전의 최소 개수
  // f(n) = min(f(n), f(n-coin) + 1)

  // dp 배열 초기화: 모든 금액을 만드는데 필요한 동전 개수를 불가능한 값(amount+1)으로 설정
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0; // 0원은 0개의 동전으로 만들 수 있음
  coins.forEach((coin) => {
    for (let i = coin; i < dp.length; i++) {
      // dp[i]: 기존에 계산된 i원을 만드는 최소 동전 개수
      // dp[i-coin] + 1: (i-coin)원에 현재 동전 하나를 추가하여 i원을 만드는 경우
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  });
  // 목표 금액을 만들 수 없으면 -1 반환, 가능하면 최소 동전 개수 반환
  return dp[amount] < amount + 1 ? dp[amount] : -1;
};
