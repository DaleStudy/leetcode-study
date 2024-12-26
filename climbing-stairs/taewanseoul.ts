/**
 * 70. Climbing Stairs
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 *
 * https://leetcode.com/problems/climbing-stairs/description/
 */
function climbStairs(n: number): number {
  if (n <= 2) {
    return n;
  }

  let prev = 1;
  let cur = 2;

  for (let i = 3; i < n + 1; i++) {
    const next = prev + cur;
    prev = cur;
    cur = next;
  }

  return cur;
}

// O(n) time
// O(1) space
