/**
 * 시간 복잡도: O(log n)
 * 공간 복잡도: O(1)
 */
function hammingWeight(n: number): number {
  let sum = 0;

  while (n > 0) {
    sum += Math.abs(n % 2);
    n = Math.floor(n / 2);
  }
  return (sum += n);
}
