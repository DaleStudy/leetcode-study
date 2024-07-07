// Time Complexity: O(n)
// Space Complexity: O(n)

var rob = function (nums) {
  // to rob a linear list of houses
  function robLinear(houses) {
    let prev1 = 0;
    let prev2 = 0;

    for (let money of houses) {
      let temp = Math.max(prev1, money + prev2);
      prev2 = prev1;
      prev1 = temp;
    }

    return prev1;
  }

  // 1. excluding the last house (rob from first to second-to-last)
  // 2. excluding the first house (rob from second to last)
  let robFirstToSecondLast = robLinear(nums.slice(0, -1));
  let robSecondToLast = robLinear(nums.slice(1));

  // return the maximum money
  return Math.max(robFirstToSecondLast, robSecondToLast);
};
