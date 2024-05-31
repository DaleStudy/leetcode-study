/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const set = new Set(nums);
  let longestStreak = 0;

  for (const num of set) {
    // Check if it's the start of a sequence
    if (!set.has(num - 1)) {
      let currentNum = num;
      let currentStreak = 1;

      // Find the length of the sequence
      while (set.has(currentNum + 1)) {
        currentNum += 1;
        currentStreak += 1;
      }

      longestStreak = Math.max(longestStreak, currentStreak);
    }
  }

  return longestStreak;
};

/**
 * Time Complexity: O(n) where n is the length of the input array.
 * Reason:
 *   Creating the Set: O(n)
 *   Iterating Through the Set: O(n)
 *   Checking for the Start of a Sequence: O(n)
 *   Finding the Length of the Sequence: O(n) across all sequences
 *   Tracking the Longest Sequence: O(n)
 *
 * Space Complexity: O(n) because of the additional space used by the set.
 */
