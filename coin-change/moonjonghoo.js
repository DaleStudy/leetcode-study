/**
 * 🔢 문제 이름: coin-change
 * 🧩 문제 유형: dp
 * 💡 핵심 아이디어
 * - 금액 i를 만들 수 있는 최소 동전 수를 dp[i]에 저장
 * - 하위 문제 dp[i - coin]에서 1개를 추가하는 방식
 * - dp[0] = 0을 시작으로 bottom-up 방식으로 점화식을 채워나간다
 *
 * 📈 시간복잡도: O(n * k) — n = amount, k = coins.length
 * 📦 공간복잡도: O(n)
 */

function coinChange(coins, amount) {
  //1.  dp 배열을 설정합니다.
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  //2. 탐색하여 최소동전의 개수를 담은 dp배열을 채웁니다.
  for (let i = 1; i <= amount; i++) {
    for (let coin of coins) {
      //코인을 사용가능하다면, 비교교
      if (i - coins >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }
  // 3. amount 값이 Infinity 라면 불가능하다라는 의미기떄문에 -1 리턴턴
  return dp[amount] === Infinity ? -1 : dp[amount];
}
