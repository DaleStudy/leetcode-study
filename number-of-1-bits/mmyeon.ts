/**
 * @link https://leetcode.com/problems/number-of-1-bits/description/
 *
 * 접근 방법 :
 *  - n을 2로 나누면서 나머지가 1인 경우 카운트를 업데이트한다.
 *
 * 시간복잡도 : O(logn)
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

/**
 * 접근 방법 : 비트 연산자 활용
 *  - n & 1 : n의 마지막 비트가 1인지 확인하여 bitCount 업데이트
 *  - n >>>= 1 : 오른쪽 시프트로 n을 1비트씩 이동
 */
function hammingWeight(n: number): number {
  let bitCount = 0;
  while (n >= 1) {
    bitCount += n & 1;

    n >>>= 1;
  }

  return bitCount;
}
