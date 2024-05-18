/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 2) {
    return n;
  }

  let [firstStair, secondStair] = [1, 2];
  let thirdStair;

  for (let i = 3; i <= n; i++) {
    thirdStair = firstStair + secondStair;

    [firstStair, secondStair] = [secondStair, thirdStair];
  }

  return thirdStair;
};

// Time Complexity: O(n)
// Reason: The function uses a loop that iterates from 3 to n,
//         which means it runs in linear time with respect to n.

// Space Complexity: O(1)
// Reason: The function uses a fixed amount of extra space
//         (a few integer variables: first, second, and third).
//         It does not use any additional data structures
//         that grow with the input size n.
