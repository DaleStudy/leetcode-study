/**
 * @param nums - 정렬된 정수 배열
 * @param target - 찾는 수
 * @returns - 왼쪽으로 몇 번 이동해야 target을 찾는지 반환 없으면 -1
 * @description
 * - 풀이 1. 이게 통과가 되네?
 * - 풀이 2. 중앙 부터 좌우 값을 줄여가며 탐색 - 이진탐색
 */

// function search(nums: number[], target: number): number {
//   let result = -1;
//   for (let i = 0; i < nums.length; i++) {
//     if (nums[i] === target) {
//       result = i;
//     }
//   }

//   return result;
// }

function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    if (
      (nums[left] <= target && target < nums[mid]) ||
      (nums[mid] < nums[left] && target > nums[right]) ||
      (nums[left] > nums[mid] && target < nums[mid])
    ) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return -1;
}

const nums = [4, 5, 6, 7, 0, 1, 2];
const target = 0;
search(nums, target);


