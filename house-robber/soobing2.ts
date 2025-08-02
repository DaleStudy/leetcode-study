/**
 * 문제 유형: DP
 *
 * 문제 설명
 * - 바로 옆집을 한번에 털 수 없을때, 최대로 털 수 있는 돈을 구하는 문제
 * - 함정은, 홀수의 합 vs 짝수의 합만 비교해서는 안된다. 2개 초과해서 털 수 있는 경우가 있음 (ex. [2, 1, 1, 2])
 *
 * 아이디어
 * - DP 문제 답게 Top-down, Bottom-up 두 개 다 풀 수 있음
 */

function robBottomUp(nums: number[]): number {
  const n = nums.length;
  const dp = Array(n).fill(0);

  if (n === 1) return nums[0];
  if (n === 2) return Math.max(nums[0], nums[1]);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }

  return dp[n - 1];
}

function robTopDown(nums: number[]): number {
  const n = nums.length;
  const memo = new Map<number, number>();

  const dp = (i: number) => {
    if (i < 0) return 0;
    if (memo.has(i)) return memo.get(i);

    const res = Math.max(dp(i - 1)!, dp(i - 2)! + nums[i]);
    memo.set(i, res);
    return res;
  };
  return dp(n - 1)!;
}
