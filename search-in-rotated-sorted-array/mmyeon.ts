/**
 * @link https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * 접근 방법 :
 *  - O(log n)으로 풀어야 하니까 이진 탐색으로 탐색 범위 좁히기
 *  - pivot 인덱스 찾고, pivot 기준으로 target이 속하는 범위에서 탐색하기
 *
 * 시간복잡도 : O(log n)
 *  - 배열 범위를 계속 줄여나가므로 O(log n)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */

function search(nums: number[], target: number): number {
  let start = 0,
    end = nums.length - 1;

  // pivot 인덱스 찾기
  while (start < end) {
    const mid = Math.floor((start + end) / 2);
    if (nums[mid] > nums[end]) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }

  const pivot = start;
  start = 0;
  end = nums.length - 1;

  // pivot 기준으로 target이 포함된 범위로 좁히기
  if (nums[pivot] <= target && target <= nums[end]) {
    start = pivot;
  } else {
    end = pivot - 1;
  }

  // target 인덱스 찾기 위해서 이진 탐색 실행
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);

    if (nums[mid] === target) return mid;
    if (nums[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return -1;
}
