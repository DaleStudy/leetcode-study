// Time Complexity: O(n)
// Space Complexity: O(1)

var maxSubArray = function (nums) {
  let maxSum = nums[0];
  let currentSum = 0;

  // iterate through the array
  for (let i = 0; i < nums.length; i++) {
    // if currentSum is negative, reset it to 0
    if (currentSum < 0) {
      currentSum = 0;
    }

    // add the current element to currentSum
    currentSum += nums[i];

    // update maxSum if currentSum is greater
    if (currentSum > maxSum) {
      maxSum = currentSum;
    }
  }

  // return the maximum subarray sum
  return maxSum;
};
