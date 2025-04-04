/**
 *
 * 접근 방법 :
 *  - 최적의 해를 구하기 위해서 dp 사용
 *  - 현재 인덱스까지 훔칠 수 있는 가장 큰 값을 dp에 저장
 *
 * 시간복잡도 : O(n)
 *  - nums 배열을 1회만 순회하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - nums 배열 크기만큼 dp 배열에 저장
 */
function rob(nums: number[]): number {
  const dp: number[] = [];

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }

  return dp[nums.length - 1];
}

/**
 *
 * 접근 방법 : 공간 복잡도 O(1)로 최적화
 * - 이전 두 값만 저장하는 방식으로 개선
 *
 * 시간복잡도 : O(n)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  let prev2 = nums[0];
  let prev1 = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const current = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
}
