/**
 * @param {number} n
 * @return {number}
 */

const climbStairs = (n) => {
  if (n <= 2) return n;

  let prev1 = 1;
  let prev2 = 2;

  for (let i = 3; i <= n; i++) {
    const current = prev1 + prev2;
    prev1 = prev2;
    prev2 = current;
  }

  return prev2;
};
