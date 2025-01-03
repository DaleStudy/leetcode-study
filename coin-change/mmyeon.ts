/**
 *
 * 접근 방법 :
 * - 동전 최소 개수 구하는 문제니까 DP로 풀기
 * - 코인마다 순회하면서 동전 개수 최소값 구하기
 * - 기존값과 코인을 뺀 값 + 1 중 작은 값으로 업데이트
 *
 * 시간복잡도 : O(n * m)
 * - 코인 개수 n만큼 순회
 * - 각 코인마다 amount 값(m) 될 때까지 순회
 *
 * 공간복잡도 : O(m)
 * - amount 만큼 dp 배열 생성
 *
 */
function coinChange(coins: number[], amount: number): number {
  const dp = Array(amount + 1).fill(Number.MAX_VALUE);
  dp[0] = 0;

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp[amount] === Number.MAX_VALUE ? -1 : dp[amount];
}
