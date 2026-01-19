/**
 * @pseudocode
 * - Map 으로 탐색이 가능하도록 정리
 * - nums의 length 만큼 돌며 없는 값 체크
 *
 * @param nums - 숫자 배열
 * @returns - 순서 상 없는 숫자 반환
 * @description
 * - 다른 답 보니 다 더해서 없는 값 찾으면 그만이구나;;;
 *
 */

// function missingNumber(nums: number[]): number {
//   const numMap = new Map();

//   for (const num of nums) {
//     numMap.set(num, true);
//   }

//   for (let i = 0; i < nums.length; i++) {
//     if (!numMap.has(i)) {
//       return i;
//     }
//   }
//   return nums.length;
// }

function missingNumber(nums: number[]): number {
  let test = 0;
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    test += i;
    sum += nums[i];
  }

  test += nums.length;

  return Math.abs(test - sum);
}

const nums = [3, 0, 1];
missingNumber(nums);



