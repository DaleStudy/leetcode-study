/**
 * @param nums - 정렬되지 않은 정수 배열
 * @returns - 가장 긴 연속 요소 길이
 *
 * @description
 * 1. 객체의 정렬 활용 방식 - O(n log n) -> 결국 key 정렬 시 n log n 발생
 * 2. 정렬 없이 key find 방식 - O(n) -> 시작점일 경우만 판단, 모든 num에 대해 돌지 않음
 */

// function longestConsecutive(nums: number[]): number {
//   const obj = nums.reduce((acc, cur) => {
//     acc[cur] = (acc[cur] || 0) + 1;
//     return acc;
//   }, {});
//   let cnt = 1;
//   let answer = 0;

//   const keys = Object.keys(obj);

//   for (let i = 1; i < keys.length; i++) {
//     if (Number(keys[i]) === Number(keys[i - 1]) + 1) {
//       cnt++;
//     } else {
//       answer = Math.max(answer, cnt);
//       cnt = 1;
//     }
//   }

//   answer = Math.max(answer, cnt);

//   return answer;
// }

function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let answer = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let current = num;
      let cnt = 1;

      while (numSet.has(current + 1)) {
        current++;
        cnt++;
      }

      answer = Math.max(answer, cnt);
    }
  }
  return answer;
}

