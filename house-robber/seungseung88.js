// 시간 복잡도: O(n) 한 번의 루프만 돎
// 공간 복잡도: O(n) nums와 같은 길이의 dp배열 생성

const rob = (nums) => {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  const dp = Array(nums.length - 1).fill(0);

  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i += 1) {
    dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
  }

  return dp[nums.length - 1];
};
