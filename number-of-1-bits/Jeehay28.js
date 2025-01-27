// 💪 Optimized Approach: Brian Kernighan's Algorithm
// Brian Kernighan's algorithm is a very efficient way to count the number of set bits in a number.
// It works by repeatedly turning off the rightmost set bit.

// Time Complexity: O(k), where k is the number of set bits (1s) in the binary representation of n.
// - Binary representation of 5 : 101

// Space Complexity: O(1)

/**
 *
 * @param {number} n - The number whose set bits need to be counted.
 * @return {number} - The number of set bits (1s) in the binary representation of n.
 */

var hammingWeight = function (n) {
  let cnt = 0;

  while (n > 0) {
    cnt += 1;
    n = n & (n - 1); // removes the rightmost set bit (1) in the binary representation of n, and the other bits remain unchanged
  }
  return cnt;
};

// 💪 Improved versiion
// TC: O(log n)
// SC: O(1)
// var hammingWeight = function(n) {

//     let cnt = 0;

//     while(n > 0) {
//         cnt += n % 2;
//         n = Math.floor(n / 2)
//     }
//     return cnt;

// };

// 💪 My own approach
// Time Complexity: O(log n)
// Space Complexity: O(log n)

/**
 * Time Complexity: O(log n)
 * - The operation `n.toString(2)` converts the number into its binary representation, which takes O(log n) time, where 'n' is the input number.
 * - The `replaceAll("0", "")` operation goes through the binary string to remove all '0' characters, which is O(log n) as the binary string has a length of log(n).
 * - The `.length` operation to count the '1' characters is O(log n) as well.
 * - Overall, the time complexity is O(log n) since we are iterating over the binary string twice (once to convert and once to remove zeros).

 * Space Complexity: O(log n)
 * - The binary representation of the number is stored as a string, which takes O(log n) space, where log(n) is the length of the binary string.
 * - Therefore, the space complexity is O(log n) because of the space used to store the binary string during the conversion process.
 */

/**
 * @param {number} n
 * @return {number}
 */

// var hammingWeight = function (n) {
//     let binary = n.toString(2).replaceAll("0", "").length;

//     return binary;
//   };


