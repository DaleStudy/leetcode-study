/**
 *
 * @param nums - 정수 배열
 * @returns - 배열에 같은 값이 2번 이상 반복 되면 true 아님 false
 *
 * @description
 * 1. Set으로 길이 비교 후 길이에 따라 반환 O(n) -> Set 생성 시 입력된 배열 요소 순회
 * 2. Map으로 간단하게 체크 만약 has 시 true 반환 O(n)
 * 3. Map, Set 없이 객체로 체크 O(n)
 */

function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size ? true : false;
}

// function containsDuplicate(nums: number[]): boolean {
//   const map = new Map();
//   for (const num of nums) {
//     if (map.has(num)) {
//       return true;
//     }
//     map.set(num, 1);
//   }
//   return false;
// }

// function containsDuplicate(nums: number[]): boolean {
//   const obj: Record<number, number> = {};

//   for (const num of nums) {
//     obj[num] = (obj[num] || 0) + 1;
//   }

//   return Object.keys.length !== nums.length ? true : false;
// }

const exam01 = containsDuplicate([1, 2, 3, 1]);
const exam02 = containsDuplicate([1, 2, 3, 4]);

console.log(exam01, exam02);

