/**
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(1)
 */
function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev2 = 1;
  let prev1 = 2;
  let current = 0;

  for (let i = 3; i <= n; i++) {
    current = prev2 + prev1;
    prev2 = prev1;
    prev1 = current;
  }
  return current;
}
