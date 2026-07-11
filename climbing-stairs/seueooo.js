/**
 * @param {number} n
 * @return {number}
 *
 * 풀이
 * 1. dp를 사용하여 각 계단까지 올라갈 수 있는 방법의 수를 계산한다.
 * 2. dp[i]는 i번째 계단까지 올라갈 수 있는 방법의 수를 나타낸다.
 * 3. dp[i] = dp[i - 1] + dp[i - 2] : 마지막에 한 번에 1계단을 올라온 경우와 2계단을 올라온 경우를 합친다.
 * 시간 복잡도 - O(n) : 배열을 한 번 순회
 * 공간 복잡도 - O(n) : dp 배열 생성
 */
var climbStairs = function (n) {
  let dp = [];
  dp[0] = 0;
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};
