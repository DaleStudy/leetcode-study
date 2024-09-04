/**
 * @param {number} n
 * @return {number}
 */
/**
 * Note: DP
 * 결국 1개 전의 값에서 1칸을 더 가거나, 2개 전의 값에서 2칸을 더 가는 경우의 수가 생긴다.
 * 1일때에는 1칸을 가는 방법의 경우 뿐이지만, 2일때에는 0칸 가는 것에서 2칸을 가거나 1칸을 가는 것에서 1칸을 더 갈 수 있다.
 * 3일 때에는 1까지 갔을 경우에서 2칸을 더 가거나, 2까지 갔을 경우에서 1칸을 더 가면 되니까 1까지 갔을 경우의 수 + 2까지 갔을 경우의 수
 *
 *
 * Runtime: 41ms, Memory: 48.95MB
 * Time complexity: O(n)
 * Space complexity: O(n)
 *
 */

var climbStairs = function (n) {
  const dp = Array(n).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i < n + 1; i++) {
    dp[i] = dp[i - 2] + dp[i - 1];
  }

  return dp[n];
};
