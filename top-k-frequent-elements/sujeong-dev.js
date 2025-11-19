/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 * 
 * 시간복잡도 계산
 * for loop가  O(n)
 * reduce가 O(n)
 * sort가 O(n log n)
 * => O(n log n)
 */
var topKFrequent = function (nums, k) {
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    if (result.find((el) => el.key == nums[i])) continue;
    const count = nums.reduce((cnt, el) => cnt + (nums[i] === el), 0);
    result.push({ key: nums[i], value: count });
  }

  return result
    .sort((a, b) => b.value - a.value)
    .slice(0, k)
    .map((el) => el.key);
};

/**
 * Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */
