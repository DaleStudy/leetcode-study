/*
* 시간 복잡도: O(n)
* 공간 복잡도: O(1)
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let max = nums[0];
  let result = nums[0];

  for (let index = 1; index < nums.length; index++) {
    const num = nums[index];
    result = Math.max(result + num, num);
    max = Math.max(max, result);
  }

  return max;
};