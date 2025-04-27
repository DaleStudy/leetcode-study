/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  // 초기값 설정: 현재까지의 최대합과 전체 최대합을 배열의 첫 번째 값으로 초기화
  let currentSum = nums[0];
  let maxSum = nums[0];

  // 두 번째 원소부터 순회
  for (let i = 1; i < nums.length; i++) {
    // 이전까지의 합에 현재 원소를 더할지, 아니면 현재 원소부터 새로 시작할지 결정
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    // 전체 최대값 갱신
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
};
