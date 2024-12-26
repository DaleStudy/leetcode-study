/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // n+1 배열을 만들고 0으로 초기화
  const dp = new Array(n + 1).fill(0);

  // 인덱스 0번과 1번은 1로 초기화
  dp[0] = 1;
  dp[1] = 1;

  // 이전계단과 그 이전 계단의 합이 계단을 올라갈 수 있는 총합
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};

console.log(climbStairs(5));
