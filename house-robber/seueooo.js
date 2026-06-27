/**
 * 풀이
 * dp 사용하여 각 집까지 털 수 있는 최대 금액을 계산한다.
 * dp[i]는 0번 집부터 i번 집까지만 고려했을 때 털 수 있는 최대 금액을 나타낸다.
 * 시간 복잡도 - O(n) : 배열을 한 번 순회
 * 공간 복잡도 - O(n) : dp 배열 생성
 */
var rob = function (nums) {
  const n = nums.length;
  let dp = new Array(n);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }
  return dp[n - 1];
};
