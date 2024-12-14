// Time complexity: O(nlogn)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const frequencyDict = new Map();

  for (const num of nums) {
    if (frequencyDict.has(num)) {
      frequencyDict.set(num, frequencyDict.get(num) + 1);
    } else {
      frequencyDict.set(num, 1);
    }
  }

  const entries = [...frequencyDict.entries()];
  entries.sort((a, b) => b[1] - a[1]);

  return entries.slice(0, k).map((entry) => entry[0]);
};
