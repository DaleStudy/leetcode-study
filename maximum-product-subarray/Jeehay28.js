/**
 * @param {number[]} nums
 * @return {number}
 */

// ✅ DP approach
// Time Complexity: O(n)
// Space Complexity: O(1)
var maxProduct = function (nums) {
  // Track the minimum and maximum product ending at the current position
  // Consider three possibilities for each element:
  // 1. Current number
  // 2. Previous min product * current number (to handle negative numbers)
  // 3. Previous max product * current number (to handle negative numbers)

  let maxProduct = nums[0];
  let previousMinProduct = 1;
  let previousMaxProduct = 1;

  for (const current of nums) {
    const temp1 = previousMinProduct * current;
    const temp2 = previousMaxProduct * current;

    // Update min and max product
    previousMinProduct = Math.min(current, temp1, temp2);
    previousMaxProduct = Math.max(current, temp1, temp2);

    // Update maxProduct
    maxProduct = Math.max(maxProduct, previousMaxProduct);
  }

  return maxProduct;
};

// 🤔 more efficient than the previous one, but there might be a further optimization
// using dynamic programming approach to reduce the complexity to O(n)
// Time Complexity: O(n^2)
// Space Complexity: O(1)

// var maxProduct = function (nums) {
//   let max = nums[0];

//   for (let s = 0; s < nums.length; s++) {
//     let temp = 1;
//     for (let e = s; e < nums.length; e++) {
//       temp *= nums[e];
//       max = Math.max(max, temp);
//     }
//   }
//   return max;
// };

// 😱 Time Limit Exceeded!
// Time Complexity: O(n^3)
// Space Complexity: O(1)
// var maxProduct = function (nums) {
//   let max = nums[0];

//   for (let s = 0; s < nums.length; s++) {
//     for (let e = s; e < nums.length; e++) {
//       let temp = 1;

//       for (let i = s; i <= e; i++) {
//         temp *= nums[i];
//       }

//       max = Math.max(max, temp);
//     }
//   }

//   return max;
// };


