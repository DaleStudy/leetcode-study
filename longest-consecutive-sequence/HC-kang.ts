/**
 * https://leetcode.com/problems/longest-consecutive-sequence/
 * T.C.: O(n)
 * S.C.: O(n)
 */
function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let max = 0;

  for (const num of numSet) {
    if (numSet.has(num - 1)) {
      continue;
    }

    let count = 0;
    while (numSet.has(num + count)) {
      count++;
    }

    if (count > max) max = count;
  }

  return max;
}
