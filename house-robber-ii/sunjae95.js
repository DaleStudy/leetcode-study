/**
 * @description
 * 점화식: dp[i] = Math.max(dp[i - 1], dp[i - 2] + current);
 * 순회한다는 조건이 있으므로 다음과 같이 분기처리 할 수 있다.
 * 1. 처음이 선택 O 마지막 X
 * 2. 처음이 선택 X 마지막 상관없음
 *
 * n = length of nums
 * time complexity: O(n)
 * space complexity: O(n)
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  const hasFirst = Array.from({ length: nums.length }, (_, i) =>
    i < 2 ? nums[0] : 0
  );
  const noFirst = Array.from({ length: nums.length }, (_, i) =>
    i === 1 ? nums[i] : 0
  );
  for (let i = 2; i < nums.length; i++) {
    hasFirst[i] = Math.max(hasFirst[i - 1], hasFirst[i - 2] + nums[i]);
    noFirst[i] = Math.max(noFirst[i - 1], noFirst[i - 2] + nums[i]);
    if (i === nums.length - 1) {
      hasFirst[i] = Math.max(hasFirst[i - 1], hasFirst[i - 2]);
    }
  }

  return Math.max(hasFirst[nums.length - 1], noFirst[nums.length - 1]);
};
