/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const countMap = new Map();
  for (const num of nums) {
    if (countMap.has(num)) {
      countMap.set(num, countMap.get(num) + 1);
    } else {
      countMap.set(num, 1);
    }
  }
  const countArr = [...countMap];
  countArr.sort((a, b) => b[1] - a[1]);

  const res = countArr.slice(0, k).map((count) => count[0]);
  return res;
};
