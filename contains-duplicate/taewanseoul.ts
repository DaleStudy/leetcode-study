/**
 * 217. Contains Duplicate
 * Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 * https://leetcode.com/problems/contains-duplicate/description/
 */
function containsDuplicate(nums: number[]): boolean {
  const set = new Set<number>();

  for (let i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) {
      return true;
    }
    set.add(nums[i]);
  }

  return false;
}

// TC: O(n)
// https://262.ecma-international.org/15.0/index.html#sec-get-set.prototype.size
// Set objects must be implemented using either hash tables or other mechanisms that, on average, provide access times that are sublinear on the number of elements in the collection. The data structure used in this specification is only intended to describe the required observable semantics of Set objects. It is not intended to be a viable implementation model.
