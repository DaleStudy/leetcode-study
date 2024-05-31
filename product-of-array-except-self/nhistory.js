/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const len = nums.length;
  const lastIndex = len - 1;

  // Declare prefix, postfix array
  let prefix = new Array(len).fill(1);
  let postfix = new Array(len).fill(1);

  // Iterate loop to add prefix[i-1]*nums[i] values into prefix array
  prefix[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    prefix[i] = prefix[i - 1] * nums[i];
  }

  // Iterate loop to add postfix[i]*nums[i-1] values into postfix array
  postfix[lastIndex] = nums[lastIndex];
  for (let i = lastIndex; i >= 1; i--) {
    postfix[i - 1] = postfix[i] * nums[i - 1];
  }

  // Make output array with prefix and postfix arrays
  let output = new Array(len).fill(1);

  // First index value is equal to postfix[1]
  output[0] = postfix[1];
  // Last index value is equal to prefix[lastIndex-1]
  output[lastIndex] = prefix[lastIndex - 1];
  for (let i = 1; i < len - 1; i++) {
    output[i] = prefix[i - 1] * postfix[i + 1];
  }

  return output;
};

// TC: O(n)
// SC: O(n)
