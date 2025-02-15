/**
 *@link https://leetcode.com/problems/sum-of-two-integers/description/
 *
 * 접근 방법 :
 *  - 비트 AND 연산자(&) 사용해서 자리 올림이 필요한 비트 계산하고 왼쪽 시프트(<<)로 자리 올림값을 다음 자리로 이동
 *  - 비트 XOR 연산자(^) 사용해서 자리 올림 제외한 자리합 계산하고 a값 업데이트
 *  - 자리 올림값이 0이 될 때까지 자리 올림 반복
 *  - 자리 올림 없으면 최종합이 저장된 a 리턴
 *
 *
 * 시간복잡도 : O(k)
 *  - k는 숫자의 비트 수, 최대 k번 반복
 *
 * 공간복잡도 : O(1)
 * - 고정된 변수만 사용
 *
 */

function getSum(a: number, b: number): number {
  while (b) {
    // 자리 올림 계산
    const carry = (a & b) << 1;
    // 자리합 업데이트 (같은 비트 = 0, 다른 비트 = 1)
    a ^= b;
    b = carry;
  }

  return a;
}
