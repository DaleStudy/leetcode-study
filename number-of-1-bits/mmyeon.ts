/**
 * @link https://leetcode.com/problems/number-of-1-bits/description/
 *
 * 접근 방법 :
 *  - n을 2로 나누면서 나머지가 1인 경우 카운트를 업데이트한다.
 *
 * 시간복잡도 : O(log(n))
 *  - 숫자의 비트 길이만큼 반복
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function hammingWeight(n: number): number {
  let bitCount = 0;
  while (n >= 1) {
    bitCount += n % 2;

    n = Math.floor(n / 2);
  }

  return bitCount;
}

// 비트 연산자 활용하는 방법
function hammingWeight(n: number): number {
  let bitCount = 0;
  while (n >= 1) {
    bitCount += n & 1;

    n >>>= 1;
  }

  return bitCount;
}
