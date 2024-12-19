// https://leetcode.com/problems/climbing-stairs/
/**
 * @SC `O(1)`
 * @TC `O(n)`
 */
function climbStairs(n: number): number {
  if (n <= 2) {
    return n;
  }

  let prev1 = 1;
  let prev2 = 2;

  for (let i = 2; i < n; i++) {
    let temp = prev1;
    prev1 = prev2;
    prev2 = temp + prev2;
  }
  return prev2;
}
