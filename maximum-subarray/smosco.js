/**
 * Maximum Subarray - 브루트포스 (완전탐색)
 *
 * 핵심 아이디어:
 * - 모든 가능한 연속 부분 배열의 합을 계산하여 최댓값 찾기
 * - i번째부터 j번째까지의 합을 누적하면서 계산
 *
 * 시간 복잡도: O(n²) - 이중 반복문으로 모든 구간 탐색
 * 공간 복잡도: O(1) - 변수 몇 개만 사용
 */
const maxSubArray = (nums) => {
  const n = nums.length;
  let maxSoFar = nums[0];

  for (let i = 0; i < n; i++) {
    let currentSum = 0;
    for (let j = i; j < n; j++) {
      currentSum += nums[j]; // i부터 j까지의 누적 합
      maxSoFar = Math.max(maxSoFar, currentSum);
    }
  }

  return maxSoFar;
};

/**
 * Maximum Subarray - Kadane's Algorithm
 *
 * 핵심 아이디어:
 * - 각 위치에서 "현재 숫자만으로 새로 시작 vs 이전 합에 현재 숫자 추가" 중 더 큰 값 선택
 * - currentMax = max(현재 숫자, 지금까지 합 + 현재 숫자)
 * - 즉, 이전까지의 합이 현재에 도움이 안 되면 버리고 새로 시작
 *
 * 시간 복잡도: O(n) - 배열을 한 번만 순회
 * 공간 복잡도: O(1) - 변수 두 개만 사용
 */
const maxSubArrayKadane = (nums) => {
  let currentMax = nums[0]; // 현재 위치까지의 최대 합
  let globalMax = nums[0]; // 전체 최대 합

  for (let i = 1; i < nums.length; i++) {
    // 핵심: 이전 합에 더할지 vs 새로 시작할지
    currentMax = Math.max(nums[i], currentMax + nums[i]);
    globalMax = Math.max(globalMax, currentMax);
  }

  return globalMax;
};
