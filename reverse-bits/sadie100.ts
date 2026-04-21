/**
 n의 뒤의 자리에서부터 비트로 변환해서 result에 붙이고, result 비트를 앞으로 당기는 일을 32번 반복해서 뒤집어진 비트를 만든다

 시간복잡도 : O(1) - 비트 연산
 공간복잡도 : O(1)
 */

function reverseBits(n: number): number {
  let result = 0

  for (let i = 0; i < 32; i++) {
    let bit = n & 1

    result = (result << 1) | bit

    n = n >>> 1
  }
  return result >>> 0
}
