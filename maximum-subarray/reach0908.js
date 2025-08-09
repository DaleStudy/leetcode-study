/**
 * 시간복잡도: O(n)
 * 시간: 4ms
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let maxResult = nums[0];
  let curResult = nums[0];

  for (let i = 1; i < nums.length; i += 1) {
    const num = nums[i];
    // 지금까지 누적합 vs 현재 날짜
    result = Math.max(curResult + num, num);
    maxResult = Math.max(maxResult, curResult);
  }

  return maxResult;
};
