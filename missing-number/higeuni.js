/**
 * @param {number[]} nums
 * @return {number}
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */

var missingNumber = function(nums) {
  const sumOfNums = nums.reduce((acc, curr) => acc + curr, 0);
  const sumOfTotalNumbers = (nums.length * (nums.length + 1)) / 2;
  return sumOfTotalNumbers - sumOfNums;
};

