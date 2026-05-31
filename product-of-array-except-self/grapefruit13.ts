/**
 * @description Return an array where each element is the product of all numbers in nums excep nums
 * @param {number[]} nums
 * @returns {number[]}
 */
function productExceptSelf(nums: number[]): number[] {
  // result array (stores prefix products first)
  const answer = new Array(nums.length);

  // prefix product: product of all elements to the left of i
  answer[0] = 1;
  for (let i = 1; i < nums.length; i++) {
    // multiply previous prefix with the previous number
    answer[i] = answer[i - 1] * nums[i - 1];
  }

  // suffix product: product of all elements to the right of i
  let rightProduct = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    // multiply prefix product and suffix product
    answer[i] *= rightProduct;
    // update suffix product for next iteration
    rightProduct *= nums[i];
  }

  return answer;
}
