/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

/**
 * Runtime: 64ms, Memory: 53.31MB
 *
 * Time complexity: O(NlogN)
 *  - frquentEntries.sort: NlogN
 * Space complexity: O(n)
 *
 * **/

var topKFrequent = function (nums, k) {
  let answer = [];

  const frequent = {};
  for (const num of nums) {
    frequent[num] = frequent[num] ? frequent[num] + 1 : 1;
  }

  const frequentEntries = Object.entries(frequent);
  frequentEntries.sort((a, b) => b[1] - a[1]);

  const topK = frequentEntries.slice(0, k).map((i) => i[0]);

  return topK;
};
