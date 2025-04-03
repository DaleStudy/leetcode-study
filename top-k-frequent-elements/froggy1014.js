/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const map = new Map();
  for (let n = 0; n < nums.length; n++) {
    map.has(nums[n])
      ? map.set(nums[n], map.get(nums[n]) + 1)
      : map.set(nums[n], 1);
  }

  return Array.from(map.entries())
    .sort(([key1, value1], [key2, value2]) => value2 - value1)
    .slice(0, k)
    .map((v) => v[0]);
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
