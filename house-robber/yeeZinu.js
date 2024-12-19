var rob = function (nums) {
  const n = nums.length;

  // 길이가 1이라면
  if (n === 1) {
    return nums[0];
  }

  // nums의 길이만큼 0으로 초기화된 배열
  const dp = Array(n).fill(0);

  // 0번은 nums[0]
  dp[0] = nums[0];
  // 1번은 0과 1중 큰것을 선택
  dp[1] = Math.max(nums[0], nums[1]);

  // i-1 과 i + i-2 의 합중 더 큰것을 선택하면됨
  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
  }
  // i가 n - 1까지 반복함
  return dp[n - 1];
};
