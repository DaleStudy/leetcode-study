/**
 * 128. Longest Consecutive Sequence
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
 *
 * You must write an algorithm that runs in O(n) time.
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 */
function longestConsecutive(nums: number[]): number {
  const set = new Set(nums);
  const sorted = [...set].sort((a, b) => a - b);

  if (sorted.length === 0) {
    return 0;
  }

  let longestSequence = 1;
  let currentSequence = 1;
  for (let i = 0; i - 1 < sorted.length; i++) {
    if (Math.abs(sorted[i + 1] - sorted[i]) === 1) {
      currentSequence++;
    } else {
      if (currentSequence > longestSequence) {
        longestSequence = currentSequence;
      }
      currentSequence = 1;
    }
  }

  return longestSequence;
}

// O(n) time
// O(n) space
