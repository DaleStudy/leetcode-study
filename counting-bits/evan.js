/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  const result = new Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    /** The number of 1's in i divided by 2, except last bit of i */
    const totalOnes = result[i >> 1];
    const lastBit = i & 1;

    result[i] = totalOnes + lastBit;
  }

  return result;
};

/**
 * Time Complexity: O(n), where n is number input
 * Reason: The algorithm processes each number from 1 to n exactly once.
 *
 * Space Complexity: O(n), where n is number input
 * Reason: The algorithm uses an array of size n + 1
 */
