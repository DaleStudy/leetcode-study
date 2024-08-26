// DP 활용하였고 메모리 축소를 위해 현재와 직전의 경우의 수만 관리하였습니다.
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
