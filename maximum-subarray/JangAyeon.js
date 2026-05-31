/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let pointer = nums[0];
  let answer = pointer;
  const N = nums.length;
  for (let idx = 1; idx < N; idx++) {
    if (nums[idx] > pointer + nums[idx]) {
      pointer = nums[idx];
    } else {
      pointer += nums[idx];
    }
    // console.log(idx, pointer)
    answer = Math.max(pointer, answer);
  }
  return answer;
};
