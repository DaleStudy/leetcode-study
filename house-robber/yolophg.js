// Time Complexity: O(n)
// Space Complexity: O(n)

var rob = function (nums) {
  // to store the maximum money that can be robbed up to each house
  let memo = new Array(nums.length).fill(-1);

  function robFrom(i) {
    // if the index is out of bounds, return 0
    if (i >= nums.length) return 0;

    // 1. rob this house and move to the house two steps ahead
    // 2. skip this house and move to the next house
    // take the maximum of these two choices
    let result = Math.max(nums[i] + robFrom(i + 2), robFrom(i + 1));

    // store the result
    memo[i] = result;

    return result;
  }

  // start robbing from the first house
  return robFrom(0);
};
