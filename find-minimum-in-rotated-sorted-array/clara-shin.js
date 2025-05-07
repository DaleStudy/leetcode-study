/**
 * 오름차순으로 정렬된 배열이 1~n번 회전된 상태에서 최소값을 찾는 문제
 * 문제 핵심:
 * 1. 배열은 원래 오름차순으로 정렬되어 있었음
 * 2. 그 배열이 1~n번 회전되었음
 * 3. 최소값을 O(log n) 시간 복잡도로 찾아야 함
 *
 * => 이 문제는 회전된 배열에서 최소값을 찾아야 함
 * => 최소값은 pivot 포인트(회전이 일어난 지점)에서 발견됨
 */

/**
 * @param {number[]} nums - 회전된 정렬 배열
 * @return {number} - 배열의 최소값
 */
var findMin = function (nums) {
  let left = 0; // 검색범위의 시작 인덱스
  let right = nums.length - 1; // 검색범위의 끝 인덱스

  // 이진 탐색
  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // 중간 값이 오른쪽 끝 값보다 크면, 최소값은 오른쪽에 있음
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    }
    // 중간 값이 오른쪽 끝 값보다 작거나 같으면, 최소값은 왼쪽에 있음 (중간 포함)
    else {
      right = mid;
    }
  }

  // 반복이 끝나면 left와 right는 같은 인덱스을 가리키고, 이 인덱스의 값(피봇포인트) = 최소값의 위치
  return nums[left];
};
