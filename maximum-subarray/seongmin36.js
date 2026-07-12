/**
이 문제의 핵심은 연결된 배열이어야 하고, 누적된 값의 합이 음수라면 과감하게 다시 시작하는 것이다.
이를 카데인 알고리즘(Kadane's Algorithm)이라고 한다.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
function maxSubArray(nums) {
  let result = nums[0];
  let cur_sum = nums[0];

  if (nums.length === 1) return nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (cur_sum <= 0) {
      cur_sum = nums[i];
    } else if (cur_sum > 0) {
      cur_sum = cur_sum + nums[i];
    }

    result = Math.max(result, cur_sum);
  }
  return result;
}
