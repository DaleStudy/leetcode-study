/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (Object.keys(obj).includes(String(nums[i]))) {
      obj[nums[i]] = obj[nums[i]] + 1;
    } else {
      obj[nums[i]] = 1;
    }
  }

  const keysArr = Object.keys(obj);
  const sortedObj = keysArr
    .sort((a, b) => obj[b] - obj[a])
    .slice(0, k)
    .map((num) => Number(num));
  return sortedObj;
};
