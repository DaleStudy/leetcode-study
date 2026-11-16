/**
 * Complexity:
 * - Time: O(n)
 * - Space:	O(n)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const set = new Set(nums);
  let longestLength = 0;

  for (const n of set) {
    if (set.has(n - 1)) continue;
    else {
      let current = n;
      let currentLength = 1;

      while (set.has(current + 1)) {
        current += 1;
        currentLength += 1;
      }

      longestLength = Math.max(longestLength, currentLength);
    }
  }

  return longestLength;
};
