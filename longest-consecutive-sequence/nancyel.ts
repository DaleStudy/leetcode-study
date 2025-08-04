/**
 * requirement: return result in linear time (O(n))
 */
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums); // O(1) lookups
  let maxLength = 0;

  for (const num of numSet) {
    // key: determine the "start" of a consecutive sequence.
    // approach: if num - 1 doesn't exist in the set → num is the start of a sequence.
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      // count consecutive numbers
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }

      maxLength = Math.max(maxLength, currentLength);
    }
  }
  return maxLength;
}
