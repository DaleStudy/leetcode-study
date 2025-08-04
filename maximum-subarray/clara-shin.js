/**
 * 최대 부분 배열 합(Maximum Subarray) 또는 카데인 알고리즘(Kadane's Algorithm)
 * 정수 배열이 주어졌을 때, 합이 최대가 되는 연속된 부분 배열을 찾아 그 합을 반환하는 문제
 *
 * DP를 사용하여 현재 위치까지의 부분합을 계산하고, 그 중 최대값을 갱신하는 방식으로 해결
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  if (nums.length === 0) return 0; // 배열이 비어있으면 0 반환
  let maxSum = nums[0]; // 최대 부분합을 저장
  let currentSum = nums[0]; // 현재 위치까지의 부분합

  for (let i = 1; i < nums.length; i++) {
    // 현재 요소를 포함한 부분합과 현재 요소만 선택하는 것 중 큰 값을 선택
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum); // 전체 최대 부분합 갱신
  }

  return maxSum;
};
