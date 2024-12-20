// 시간복잡도: O(n)
// 공간복잡도: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 2) return n;
  let prev1 = 1, prev2 = 2;
  for (let i = 3; i <= n; i++) {
    let curr = prev1 + prev2;
    prev1 = prev2;
    prev2 = curr;
  }
  return prev2;
};
