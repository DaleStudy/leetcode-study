// https://leetcode.com/problems/contains-duplicate/description/

// TC: O(n)
// SC: O(n)

function containsDuplicate(nums: number[]): boolean {
  const set = new Set(nums);
  return set.size !== nums.length;
}

function containsDuplicate(nums: number[]): boolean {
  const set = new Set();

  for (const num of nums) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }

  return false;
}

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
