// T.C. O(n)
// S.C. O(1)
function climbStairs(n: number): number {
  let p = 0;
  let q = 1;
  let t: number;
  for (let i = 0; i < n; i++) {
    t = p + q;
    p = q;
    q = t;
  }
  return q;
}
