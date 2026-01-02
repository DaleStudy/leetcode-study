/**
 * @param n - 양의 정수
 * @returns - 이진 변환 시 1의 갯수
 * @description
 * - 풀이 1: 직접 이진수로 변환하는 작업을 추가
 * - 이진 수 변환 후 배열 변경, 1만 뽑아내서 길이 반환하기
 * - 시간복잡도: O(n), 공간복잡도: O(n)
 */

// function hammingWeight(n: number): number {
//   if (n === 0) return 0;
//   let result = "";
//   while (n > 0) {
//     result = (n % 2) + result;
//     n = Math.floor(n / 2);
//   }
//   let count = 0;
//   for (const ch of result) {
//     if (ch === "1") {
//       count++;
//     }
//   }
//   return count;
// }

function hammingWeight(n: number): number {
  const bit = n
    .toString(2)
    .split("")
    .filter((v) => v === "1");

  return bit.length;
}

const n = 2147483645;

hammingWeight(n);


