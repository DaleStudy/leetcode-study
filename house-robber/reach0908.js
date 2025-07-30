/**
 * @description
 * time complexity: O(2^n)
 * space complexity: O(n)
 * 풀이 실패
 * 풀이 방법: 선택한 경우와 선택하지 않은 경우를 재귀적으로 호출하여 최대값을 반환한다.
 * @param {number[]} nums
 * @return {number}
 */
const rob = function (nums) {
  console.log(nums);
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  // 선택한 경우
  const selected = nums[0] + rob(nums.slice(2));
  // 선택하지 않은 경우
  const unselected = rob(nums.slice(1));

  const max = Math.max(selected, unselected);

  return max;
};

/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * runtime: 100ms
 * 풀이 방법: 위 풀이가 타임아웃이 남, DP로 풀어야함을 인지 후 풀이 방법 변경
 * @param {number[]} nums
 * @return {number}
 */
const robSolution2 = function (nums) {
  const dp = new Array(nums.length).fill(0);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i += 1) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }

  return dp[nums.length - 1];
};
