/**
 * 각 num을 누적된 result값에 num을 더한값과 비교해서 큰 값을 result로 유지해간다.
 * 그리고 최대 누적값을 구하기 위해 매 result를 구할때마다 최대 result를 갱신한다.
 *
 * TC: O(N)
 * SC: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let maxResult = nums[0];
  let result = nums[0];

  for (let index = 1; index < nums.length; index++) {
    const num = nums[index];
    result = Math.max(result + num, num);
    maxResult = Math.max(maxResult, result);
  }

  return maxResult;
};
