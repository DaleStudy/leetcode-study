// https://leetcode.com/problems/climbing-stairs/

// TC: O(N)
// SC: O(N)

var climbStairs = function (n) {
  const stairs = [1, 2];

  for (let i = 2; i < n; i++) {
    stairs[i] = stairs[i - 1] + stairs[i - 2];
  }

  return stairs[n - 1];
};

console.log(climbStairs(5));
