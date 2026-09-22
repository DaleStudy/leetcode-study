/**
이진탐색을 이용한 풀이

TC: O(log n)
SC: O(1)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
function findMin(nums) {
  let left = 0;
  let right = nums.length - 1;

  if (nums[left] <= nums[right]) return nums[left]; // 일자 배열인 경우

  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[mid + 1]) return nums[mid + 1]; // mid의 바로 옆에서 초기화되는 경우

    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
}
