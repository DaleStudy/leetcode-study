/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const result = [];
  const numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const currentValue = numMap.get(nums[i]);

    if (currentValue) {
      numMap.set(nums[i], currentValue + 1);
    } else {
      numMap.set(nums[i], 1);
    }
  }

  const mapToArr = [...numMap.entries()];

  mapToArr.sort((a, b) => {
    if (a[1] < b[1]) return 1;
    if (a[1] > b[1]) return -1;
    return 0;
  });

  for (let i = 0; i < k; i++) {
    result.push(mapToArr[i][0]);
  }

  return result;
};
