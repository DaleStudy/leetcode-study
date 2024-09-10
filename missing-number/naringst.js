/**
 * @param {number[]} nums
 * @return {number}
 */

/**
 * Runtime: 63ms, Memory: 51.68MB
 * Time complexity: O(nlogn)
 * Space complexity: O(nlogn)
 *
 */

var missingNumber = function (nums) {
  const n = nums.length;
  nums.sort((a, b) => a - b);

  if (!nums.includes(0)) {
    return 0;
  }
  for (let i = 0; i < n; i++) {
    if (nums[i + 1] - nums[i] !== 1) {
      return nums[i] + 1;
    }
  }
  return nums[-1];
};

/**
 * NOTE
 * if use 'sort()' -> O(nlogn)
 * if you solve this problem without using sort(), can use sum of nums
 */

var missingNumber = function (nums) {
  const sumOfNums = nums.reduce((num, total) => num + total, 0);

  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;

  if (expectedSum === sumOfNums) {
    return 0;
  } else {
    return expectedSum - sumOfNums;
  }
};

/**
 * NOTE
 * or you can subtract while adding
 */

var missingNumber = function (nums) {
  let target = 0;
  for (let i = 0; i <= nums.length; i++) {
    target += i;

    if (i < nums.length) {
      target -= nums[i];
    }
  }
  return target;
};
