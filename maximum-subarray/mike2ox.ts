/**
 * source: https://leetcode.com/problems/maximum-subarray/
 * 풀이방법: 현재 위치까지의 최대 합을 저장하면서 전체 최대 합을 갱신
 * 시간복잡도: O(n) (n: nums의 길이)
 * 공간복잡도: O(1) (상수 공간만 사용)
 */
function maxSubArray(nums: number[]): number {
  // 배열이 비어있는 경우
  if (nums.length === 0) return 0;

  let result = nums[0]; // 전체 최대 합(초기값은 첫 번째 요소)
  let current = nums[0]; // 현재 위치까지의 최대 합

  for (let i = 1; i < nums.length; i++) {
    // 현재 요소를 더한 값과 현재 요소 중 큰 값을 선택
    current = Math.max(nums[i], current + nums[i]);
    // 전체 최대 합 갱신
    result = Math.max(result, current);
  }

  return result;
}
