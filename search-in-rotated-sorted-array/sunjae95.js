/**
 * @description
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 * n = length of nums
 * time complexity: O(n)
 * space complexity: O(1)
 */
var search = function (nums, target) {
  let [start, end] = [0, nums.length - 1];
  let answer = -1;

  while (start !== end) {
    if (nums[start] === target) answer = start;
    if (nums[end] === target) answer = end;
    if (nums[start] > nums[end]) end--;
    else start++;
  }

  if (nums[start] === target) answer = start;

  return answer;
};
