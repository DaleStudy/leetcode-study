/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // Make an array to store each number of ways
  let steps = new Array(n);
  // When stairs is 1 and 2 has exact number 1 and 2
  steps[1] = 1;
  steps[2] = 2;
  // Iterate to get ways of 3 more steps stairs
  // ((n-1) + (n-2))
  for (let i = 3; i <= n; i++) {
    steps[i] = steps[i - 1] + steps[i - 2];
  }
  return steps[n];
};

// TC: O(n)
// SC: O(n)
