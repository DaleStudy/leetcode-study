/**
 * House Robber 문제
 *
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 *
 * 접근 방법:
 * - Dynamic Programming을 사용하여 각 위치에서의 최대 금액을 계산
 * - 현재 집을 털 경우: 전전 집까지의 최대값 + 현재 집의 금액
 * - 현재 집을 안 털 경우: 이전 집까지의 최대값
 * - 두 경우 중 최대값을 선택
 */
const rob = (nums) => {
  if (nums.length === 1) return nums[0];

  let prev2 = nums[0]; // 전전 집까지의 최대 금액
  let prev1 = Math.max(nums[0], nums[1]); // 이전 집까지의 최대 금액

  for (let i = 2; i < nums.length; i++) {
    const current = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
};
