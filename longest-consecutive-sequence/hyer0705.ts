function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const numSet = new Set<number>(nums);
  let longest = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let sequenceLength = 1;

      while (numSet.has(currentNum + 1)) {
        currentNum++;
        sequenceLength++;
      }

      longest = Math.max(longest, sequenceLength);
    }
  }

  return longest;
}
