/*
 * TC: O(n)
 * SC: O(n)
 * */
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums);
  let longest = 0;

  for (const num of nums) {
    if (numSet.has(num - 1)) {
      continue;
    }

    let length = 1;
    while (numSet.has(num + length)) {
      length++;
    }

    longest = Math.max(length, longest);
  }

  return longest;
}
