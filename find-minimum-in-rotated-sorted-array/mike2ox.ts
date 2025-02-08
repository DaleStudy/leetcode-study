/**
 * Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 * 풀이방법: 이진 탐색을 이용하여 최솟값을 찾음
 *
 * 시간복잡도: O(log n)
 * 공간복잡도: O(1)
 */

function findMin(nums: number[]): number {
  // 배열의 길이가 1인 경우
  if (nums.length === 1) return nums[0];

  let left: number = 0;
  let right: number = nums.length - 1;

  // 이미 정렬된 경우
  if (nums[right] > nums[0]) {
    return nums[0];
  }

  // 이진 탐색
  while (left <= right) {
    const mid: number = Math.floor((left + right) / 2);

    // 최솟값을 찾는 조건들
    if (nums[mid] > nums[mid + 1]) {
      return nums[mid + 1];
    }
    if (nums[mid - 1] > nums[mid]) {
      return nums[mid];
    }

    // 탐색 범위 조정
    if (nums[mid] > nums[0]) {
      // 최솟값은 중간점 이후에 있음
      left = mid + 1;
    } else {
      // 최솟값은 중간점 이전에 있음
      right = mid - 1;
    }
  }

  return nums[0]; // 기본값 반환
}
