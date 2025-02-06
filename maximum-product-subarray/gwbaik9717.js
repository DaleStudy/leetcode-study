// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let answer = nums[0];
  const products = Array.from({ length: nums.length + 1 }, () => null);
  products[0] = [1, 1]; // [min, max]

  for (let i = 1; i < products.length; i++) {
    const cases = [];

    // case 1
    cases.push(nums[i - 1]);

    // case 2
    cases.push(nums[i - 1] * products[i - 1][0]);

    // case 3
    cases.push(nums[i - 1] * products[i - 1][1]);

    const product = [Math.min(...cases), Math.max(...cases)];
    products[i] = product;
    answer = Math.max(answer, product[1]);
  }

  return answer;
};
