/**
 * @description
 * n = length of nums
 * time complexity: O(n)
 * space complexity: O(1)
 */
var maxSubArray = function (nums) {
  let sum = 0;
  let answer = nums[0];

  for (let end = 0; end < nums.length; end++) {
    if (sum < 0) {
      sum = nums[end];
    } else if (sum + nums[end] >= 0) {
      sum += nums[end];
    } else {
      sum = nums[end];
    }

    answer = Math.max(answer, sum);
  }
  return answer;
};
