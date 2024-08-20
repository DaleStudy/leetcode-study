/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * approach/strategy:
 * 1. brute force + hash table
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const hashTable = new Set();

  for (const num of nums) {
    if (hashTable.has(num)) return true;
    hashTable.add(num);
  }

  return false;
};
