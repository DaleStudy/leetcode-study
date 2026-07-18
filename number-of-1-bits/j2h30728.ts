/**
 * 시간 복잡도: O(n) (n: 입력값의 비트 수)
 * 공간 복잡도: O(1)
 */
function hammingWeight(n: number): number {
  let sum = 0;

  while (n > 0) {
    sum += n % 2;
    n = Math.floor(n / 2);
  }
  return (sum += n);
}
