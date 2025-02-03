/**
 * @link https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 *
 * 접근 방법 :
 * - O(logn)으로 풀어야 하니까 이진 탐색 적용
 * - 배열의 start, end 인덱스를 활용해서  최소값이 있는 방향을 탐색
 * - nums[mid] > nums[end]이면, 최소값이 오른쪽에 있으니까 start를 mid+1로 이동
 * - 반대로 nums[mid] < nums[end] 이면, 최소값이 왼쪽에 있으니까 end를 mid로 이동
 *
 * 시간복잡도 : O(logn)
 *  - 탐색 범위를 계속 절반으로 줄이니까 O(logn)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function findMin(nums: number[]): number {
  let start = 0,
    end = nums.length - 1;

  while (start < end) {
    let mid = Math.floor(start + (end - start) / 2);

    if (nums[mid] > nums[end]) start = mid + 1;
    else end = mid;
  }

  return nums[start];
}
