/**
 * Complexity:
 * - Time: O(n log n)
 * - Space:	O(n)
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    if (map.has(n)) {
      map.set(n, map.get(n) + 1);
    } else {
      map.set(n, 1);
    }
  }

  const descFrequent = [...map].sort((a, b) => b[1] - a[1]);

  const topKFrequentNums = descFrequent.slice(0, k);

  return Array.from(topKFrequentNums.map((n) => n[0]));
};
