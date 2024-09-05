// T.C. O(n)
// S.C. O(1)
function climbStairs(n: number): number {
  let p = 0;
  let q = 1;
  for (let i = 0; i < n; i++) {
    q = q + p;
    p = q - p;
  }
  return q;
}
