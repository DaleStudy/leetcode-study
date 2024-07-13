// Time Complexity: O(n)
// Space Complexity: O(1)

var maxProduct = function (nums) {
  // the current maximum product, and the current minimum product
  let maxProduct = nums[0];
  let currMax = nums[0];
  let currMin = nums[0];

  // iterate through the array starting from the second element
  for (let i = 1; i < nums.length; i++) {
    let num = nums[i];

    // update the current maximum and minimum products
    currMax = Math.max(num, num * currMax);
    currMin = Math.min(num, num * currMin);

    // update the overall maximum product
    maxProduct = Math.max(maxProduct, currMax);
  }

  // return the maximum product found
  return maxProduct;
};
