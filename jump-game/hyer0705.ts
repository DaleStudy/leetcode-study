function canJump(nums: number[]): boolean {
  const n = nums.length;

  let maximumReach = 0;

  for (let i = 0; i < n; i++) {
    if (i > maximumReach) return false;

    maximumReach = Math.max(maximumReach, i + nums[i]);
  }

  return maximumReach >= n - 1;
}
