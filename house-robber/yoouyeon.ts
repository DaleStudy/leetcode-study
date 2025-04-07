/**
 * [Idea]
 * 어떤 집을 턴다고 했을 때 최대 금액을 구하는 식은 아래와 같이 세울 수 있다.:
 * Math.max(전 집을 털었을 때의 최대 금액, 전전 집을 털었을 때의 최대 금액 + 지금 집을 털었을 때 얻는 금액) => DP
 * 연산 횟수를 줄여주기 위해서 메모 배열을 이용했다.
 *
 * [Time Complexity]
 * O(n)
 * for loop 에서 nums 배열의 각 원소에 한번씩만 접근하므로 O(n)
 *
 * [Space Complexity]
 * O(n)
 * 메모 배열을 위한 추가 공간
 */
function rob(nums: number[]): number {
  const n = nums.length;
  if (n === 1) {
    return nums[0];
  }

  // idx 집을 터는 경우 vs 안 터는 경우를 비교해서 큰 값을 저장하는 dp 배열
  const memo = new Array(n).fill(0);
  memo[0] = nums[0];
  memo[1] = Math.max(memo[0], nums[1]);

  for (let idx = 2; idx < n; idx++) {
    // idx번째 집에서의 최대 금액 = idx번째 집을 터는 경우 vs 안 터는 경우 중 최댓값
    memo[idx] = Math.max(memo[idx - 2] + nums[idx], memo[idx - 1]);
  }

  return memo[n - 1];
}
