/**
 * @param n - 32비트 정수 부호
 * @returns - 비트를 뒤집은 정수 부호
 * @description
 * - 풀이 1. 단순하게 변환, 0 채우기, 뒤집기 후 10진수로 재변환
 */
// function reverseBits(n: number): number {
//   const bits = n.toString(2).padStart(32, "0").split("").reverse().join("");

//   return parseInt(bits, 2);
// }

function reverseBits(n: number): number {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    // result를 왼쪽으로 1칸 밀어 공간생성, n의 가장 마지막 비트가 1인지 판단해 result에 할당
    result = (result << 1) | (n & 1);

    // 판단이 끝난 n의 마지막 비트를 밀어내며 다음 비트 준비
    n >>>= 1;
  }

  // 32 비트로 전환해 return
  return result >>> 0;
}

const n = 43261596;
reverseBits(n);


