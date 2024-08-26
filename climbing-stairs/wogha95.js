// TC: O(N)
// SC: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let previousStep = 0;
  let currentStep = 1;

  while (n > 0) {
    n -= 1;
    const nextStep = previousStep + currentStep;
    previousStep = currentStep;
    currentStep = nextStep;
  }

  return currentStep;
};
