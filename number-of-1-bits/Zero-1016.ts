/**
 * 시간 복잡도 O(N)
 * 공간 복잡도 O(N)
 */
function hammingWeight1(n: number): number {
  const bitNumber = n.toString(2);
  return bitNumber.split("").filter((char) => char === "1").length;
}

/**
 * 시간 복잡도 O(N)
 * 공간 복잡도 O(1)
 */
function hammingWeight2(n: number): number {
  let count = 0;
  while (n > 0) {
    count += n & 1; // 마지막 비트가 1인지 확인
    n = n >>> 1; // 우측으로 1비트 시프트 (부호 없는 우측 시프트)
  }
  return count;
}
