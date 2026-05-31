/**
 * @param nums - 오름차순 정렬된 정수 배열
 * @returns - 최솟값
 * @description
 * - 이진 탐색으로 right와 비교하며 배열의 범위를 좁혀가며 탐색
 * - left와 right가 겹치는 포인트가 최솟값
 */

function findMin(nums: number[]): number {
  let left = 0;
  let mid = Math.floor(nums.length / 2);
  let right = nums.length - 1;

  if (nums.length < 2) {
    return nums[0];
  }

  while (left < right) {
    if (nums[right] < nums[mid]) {
      left = mid + 1;
    } else {
      right = mid;
    }

    mid = Math.floor((left + right) / 2);
  }
  return nums[left];
}

const nums = [2, 1];
console.log(findMin(nums));

