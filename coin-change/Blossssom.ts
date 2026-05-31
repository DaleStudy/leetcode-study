/**
 * @param coins - 동전 종류 배열
 * @param amount - 총 금액
 * @returns - 총 사용 코인 갯수
 * @description
 * - 탐욕으로 풀면 최소 동전갯수를 구할 수 없음
 * - dp 로 풀이
 * - 1 부터 금액의 코인 사용 갯수를 추가해 가며, 이전에 구해놓은 값과 min 비교
 */
function coinChange(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(Infinity);

  dp[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
}

const coins = [1, 2, 5];
const amount = 11;
coinChange(coins, amount);

