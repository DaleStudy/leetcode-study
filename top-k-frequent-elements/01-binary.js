/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const temp = map.get(nums[i]);
    map.set(nums[i], temp !== undefined ? temp + 1 : 1);
  }
  const sortedMap = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));

  const iter = sortedMap.keys();
  const result = [];
  for (let i = 0; i < k; i++) {
    result.push(iter.next().value);
  }
  return result;
};
