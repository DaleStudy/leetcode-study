/**
 * TC: O(N^2)
 * SC: O(N)
 * N: nums.length
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  // 각자 스스로는 최소 1의 lengthOfLIS를 가짐
  const longestLength = new Array(nums.length).fill(1);
  let result = 1;

  // nums배열의 right까지 원소들 중 lengthOfLIS를 저장
  for (let right = 1; right < nums.length; right++) {
    for (let left = 0; left < right; left++) {
      if (nums[left] < nums[right]) {
        longestLength[right] = Math.max(
          longestLength[right],
          longestLength[left] + 1
        );
        result = Math.max(result, longestLength[right]);
      }
    }
  }

  return result;
};
