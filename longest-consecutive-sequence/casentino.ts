function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) {
    return 0;
  }

  const smallest = nums.sort((a, b) => a - b);
  let longest = 1;
  let sequence = 1;
  for (let i = 1; i < smallest.length; i++) {
    if (smallest[i] - smallest[i - 1] === 1) {
      sequence += 1;
    } else if (smallest[i] !== smallest[i - 1]) {
      sequence = 1;
    }
    if (longest < sequence) {
      longest = sequence;
    }
  }
  return longest;
}
