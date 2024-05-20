/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const expectedSum = (nums.length * (nums.length + 1)) / 2;
  const actualSum = nums.reduce((prev, curr) => prev + curr);

  return expectedSum - actualSum;
};

/**
 * Time Complexity: O(n)
 * Reason:
 * - Finding the maximum number in the array takes O(n) time.
 * - Calculating the target sum takes O(1) time.
 * - Iterating through the array to update the target number takes O(n) time.
 * - Checking the condition and returning the result takes O(1) time.
 * - Therefore, the overall time complexity is O(n).
 *
 * Space Complexity: O(1)
 * Reason:
 * - The algorithm uses a constant amount of extra space (variables like maxNumber, hasZero, targetNumber).
 * - No additional space proportional to the input size is used.
 * - Therefore, the overall space complexity is O(1).
 */
