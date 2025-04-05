// 1번풀이 (brute force)
// function rob(nums: number[]): number {
//   const n = nums.length;
//   if (n === 1) return nums[0];
//   if (n === 2) return Math.max(nums[0], nums[1]);

//   const dp: number[] = [];
//   dp[0] = nums[0];
//   dp[1] = Math.max(nums[0], nums[1]);

//   for (let i = 2; i < n; i++) {
//     dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
//   }

//   return dp[n - 1];
// }

// 2번풀이 (dp)
function rob(nums: number[]): number {
    if (nums.length <= 1) return nums[0] ?? 0;
  
    const dp: number[] = [];
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
  
    for (let i = 2; i < nums.length; i++) {
      dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    }
  
    return dp[nums.length - 1];
  }
  