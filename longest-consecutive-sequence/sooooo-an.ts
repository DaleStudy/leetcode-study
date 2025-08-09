function longestConsecutive(nums: number[]): number {
  if (!nums.length) return 0;

  nums.sort((a, b) => a - b);
  let longest = 1;
  let currentStreak = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) continue;
    if (nums[i] === nums[i - 1] + 1) {
      currentStreak++;
    } else {
      longest = Math.max(longest, currentStreak);
      currentStreak = 1;
    }
  }

  return Math.max(longest, currentStreak);
}

/**
 * * Runtime: 37ms / 74.15%
 * * Memory: 67.88MB / 93.54%
 */
