/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  const binary = n.toString(2).padStart(32, "0");
  const reversedBinary = binary.split("").reverse().join("");

  return parseInt(reversedBinary, 2);
};

/**
 * Time Complexity: O(1)
 * Reason:
 * - Each step involves operations on fixed-length strings or arrays (maximum length of 32).
 * - Thus, the time complexity for each operation is constant, resulting in an overall time complexity of O(1).
 *
 * Space Complexity: O(1)
 * Reason:
 * - The algorithm uses a constant amount of space for the binary string, reversed binary string, and intermediate arrays.
 * - Each of these has a fixed length of 32, so the overall space complexity is O(1).
 */
