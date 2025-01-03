/**
 * source: https://leetcode.com/problems/reverse-bits/
 * 풀이방법: 비트 연산을 이용하여 뒤집기
 * 시간복잡도: O(1)
 * 공간복잡도: O(1)
 */
function reverseBits(n: number): number {
  let result = 0;
  const bitSize = 32;
  // 32비트를 순회하면서 뒤집기
  for (let i = 0; i < bitSize; i++) {
    const bit = (n >> i) & 1; // i번째 비트 추출
    result = result | (bit << (bitSize - 1 - i)); // 뒤집은 비트를 result에 저장
  }
  return result >>> 0; // 부호비트를 제거하기 위해 0으로 비트 이동
}
