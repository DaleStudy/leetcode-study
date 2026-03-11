function longestConsecutive(nums: number[]): number {
  let result = 0;
  if (nums.length === 0) return result;

  const no_duplicate = [...new Set(nums)].sort((a, b) => a - b);
  let count = 1;

  for (let i = 0; i < no_duplicate.length; i++) {
    if (no_duplicate[i + 1] - no_duplicate[i] === 1) {
      count++;
    } else {
      result = Math.max(result, count);
      count = 1;
    }
  }

  result = Math.max(result, count);
  return result;
}

longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]); //9
longestConsecutive([100, 4, 200, 1, 3, 2]); //4
longestConsecutive([1, 0, 1, 2]); //3
longestConsecutive([]); //0
longestConsecutive([1, 2, 6, 7, 8]); //3
