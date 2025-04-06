/**
 * Finds the length of the longest consecutive elements sequence.
 * Eliminates duplicates using a Set and only starts counting when the current number is the beginning of a sequence.
 *
 * @param nums - An array of integers.
 * @returns The length of the longest consecutive sequence.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function longestConsecutive(nums: number[]): number {
  let longest = 0;
  const numSet = new Set(nums);

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let length = 1;
      while (numSet.has(num + length)) {
        length++;
      }
      longest = Math.max(length, longest);
    }
  }

  return longest;
}
