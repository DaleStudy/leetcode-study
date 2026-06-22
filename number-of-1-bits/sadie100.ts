/**
n을 이진수 변환하고 1의 개수를 센다

시간복잡도 O(N) (N은 숫자 n의 비트 개수)
 */

function hammingWeight(n: number): number {
  const binaryNum = n.toString(2)
  let result = 0
  for (let char of binaryNum) {
    if (char === '1') result += 1
  }
  return result
}
