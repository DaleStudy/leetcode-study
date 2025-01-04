/**
 * @param {number[]} nums
 * @return {number}
 */

// *** Guided approach 2: bitwise operations and avoids potential overflow issues with very large sums
// XOR method
// Time complexity: O(n)(two loops: one for numbers 0 to n  and one for array elements)
// Space complexity: O(1)

var missingNumber = function (nums) {
  // XOR with itself results in 0 : a xor a = 0
  // XOR with 0 results in the number itself : a xor 0 = a
  // XOR is commutative and associative

  const n = nums.length;

  let xor = 0;

  for (let i = 0; i <= n; i++) {
    xor ^= i;
  }

  for (any of nums) {
    xor ^= any;
  }

  return xor;
};

// *** Guided approach 1: simplicity and clarity
// Gauss' Formula (Sum of First n Numbers): n*(n+1) / 2
// Time complexity: O(n)
// Space complexity: O(1)
// var missingNumber = function (nums) {
//   const n = nums.length;
//   const expectedSum = (n * (n + 1)) / 2;
//   const actualSum = nums.reduce((acc, cur) => acc + cur, 0); // O(n)

//   const missingNum = expectedSum - actualSum;

//   return missingNum;
// };

// *** My own approach
// Time complexity: O(n^2)
// Space complexity: O(n)
// var missingNumber = function (nums) {

//     let distinctNums = new Set([]);

//     for (any of nums) {
//         if (distinctNums.has(any)) {
//             return
//         } else {
//             distinctNums.add(any)
//         }
//     }

//     const n = distinctNums.size;

//     for (let i = 0; i <= n; i++) {
//         if (!nums.includes(i)) {
//             return i;
//         }
//     }

// };
