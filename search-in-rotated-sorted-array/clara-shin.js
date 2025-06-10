/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    // 타겟을 찾았다면 인덱스 반환
    if (nums[mid] === target) {
      return mid;
    }

    // 왼쪽 절반이 정렬되어 있는 경우
    if (nums[left] <= nums[mid]) {
      // 타겟이 왼쪽 정렬된 범위에 있는지 확인
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1; // 왼쪽으로 이동
      } else {
        left = mid + 1; // 오른쪽으로 이동
      }
    }
    // 오른쪽 절반이 정렬되어 있는 경우
    else {
      // 타겟이 오른쪽 정렬된 범위에 있는지 확인
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1; // 오른쪽으로 이동
      } else {
        right = mid - 1; // 왼쪽으로 이동
      }
    }
  }

  return -1; // 타겟을 찾지 못함
};
