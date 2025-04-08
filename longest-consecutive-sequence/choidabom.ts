// https://leetcode.com/problems/longest-consecutive-sequence/

// TC: O(n)
// SC: O(n)

function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let maxLen = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let length = 1;

      while (numSet.has(currentNum + 1)) {
        currentNum += 1;
        length += 1;
      }

      maxLen = Math.max(maxLen, length);
    }
  }

  return maxLen;
}
