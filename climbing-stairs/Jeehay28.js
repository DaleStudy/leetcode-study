/**
 * @param {number} n
 * @return {number}
 */

// Time Complexity: O(n^2)
// First O(n): From the loop that runs up to n times.
// Second O(n): From the factorial calculations in each iteration.
// overall time complexity is O(n^2).

// Space Complexity: O(n)
// the factorial function's recursion has a space complexity of O(n)
// O(1) means constant space complexity. It implies that the amount of memory used does not grow with the size of the input.
// The other variables in the function only use a constant amount of space, resulting in an O(1) space usage.

var climbStairs = function (n) {
  let ways = 0;

  let maxStepTwo = Math.floor(n / 2);

  const factorial = (num) => {
    if (num === 0 || num === 1) {
      return 1;
    }

    for (let i = 2; i <= num; i++) {
      return num * factorial(num - 1);
    }
  };

  for (let i = 0; i <= maxStepTwo; i++) {
    const stepTwo = i;
    const stepOne = n - 2 * i;
    const steps = stepTwo + stepOne;

    ways += factorial(steps) / (factorial(stepTwo) * factorial(stepOne));
  }

  return ways;
};
