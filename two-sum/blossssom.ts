/**
 * @param nums - 정수 배열
 * @param target - nums 값을 더해 나올 값
 * @returns - target을 만드는 index 값
 *
 * @description
 * 1. 동일한 요소 두번 사용 금지
 * 2. 각 입력에 대해 명확한 하나의 솔루션이 있다고 가정
 *
 * @answer1
 * - O(n^2)
 *
 * @answer2
 * - O(n)
 */

// function twoSum(nums: number[], target: number): number[] {
//   for (let i = 0; i < nums.length - 1; i++) {
//     for (let j = i + 1; j < nums.length; j++) {
//       if (nums[i] + nums[j] === target) {
//         return [i, j];
//       }
//     }
//   }
//   return [];
// }

function twoSum(nums: number[], target: number): number[] {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i];
    }
    map.set(nums[i], i);
  }
  return [];
}

