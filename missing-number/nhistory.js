var missingNumber = function (nums) {
  // Get a expected summation
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;

  // Calculate summation of nums
  let numsSum = 0;
  for (let i = 0; i < n; i++) {
    numsSum += nums[i];
  }

  return expectedSum - numsSum;
};

// TC: O(n)
// SC: O(1)
