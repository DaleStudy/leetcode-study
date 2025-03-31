/**
 * Source: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 * 풀이방법: 이진탐색을 구현해서 원하는 값을 찾음
 *
 * 시간복잡도: O(log n) - 매 반복마다 탐색 범위가 절반으로 줄어듦
 * 공간복잡도: O(1) - 추가 공간을 사용하지 않고 포인터 변수만 사용
 *
 * 포인트
 *  - 문제에서 시간 복잡도를 O(log n)을 하라고 제한을 했기때문에 쉽게 이진탐색으로 풀어야 함을 파악함
 */

function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    else if (nums[mid] >= nums[left]) {
      if (nums[left] <= target && target <= nums[mid]) right = mid - 1;
      else left = mid + 1;
    } else {
      if (nums[mid] <= target && target <= nums[right]) left = mid + 1;
      else right = mid - 1;
    }
  }
  return -1;
}
