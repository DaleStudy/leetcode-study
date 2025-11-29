//풀이 1
// 시간 복잡도: O(k)
// 공간 복잡도: O(1)
// 속도: 2ms
function hammingWeight(n: number): number {
  let count = 0;
  while (n) {
    n = n & (n - 1);
    count++;
  }
  return count;
}
/*
속도는 빠르지만 복잡도가 높기 때문에 적합하지 않음.
Brian Kernighan 알고리즘을 활용한 비트 계산으로 재풀이

// 시간 복잡도: O(log n)
// 공간 복잡도: O(log n)
// 속도: 0ms
function hammingWeight(n: number): number {
  const bitNumber = n.toString(2);
  const bitString = String(bitNumber);

  const bitArray = bitString.split('').map((s) => Number(s));
  return bitArray.reduce((a, b) => a + b);
}
*/
