/**
 * 문제 설명
 * - 회전된 정렬된 배열에서 타겟 값을 찾는 문제
 * - 이진 탐색의 응용 버전
 *
 * 아이디어
 * 1) 변형된 이진 탐색 사용
 * - 중간 값과 왼쪽, 끝 값을 비교하여 왼쪽 정렬 영역인지 오른쪽 정렬 영역인지 확인
 */

function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    // mid가 왼쪽 정렬에 포함
    if (nums[mid] >= nums[left]) {
      if (target >= nums[left] && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    // mid가 오른쪽 정렬에 포함
    else {
      if (target < nums[mid] && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
}
