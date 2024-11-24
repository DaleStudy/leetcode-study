/**
 * @param {number} n, maximum 32 bit number
 * @return {number}
 */
var hammingWeight = function (n) {
  return n.toString(2).replace(/0/g, "").length;
};

/**
 * Time Complexity: O(1)
 * Reason:
 * - n.toString(2): Converts the number to a binary string, which has a fixed length of up to 32 bits. This is O(1) because the length is constant.
 * - replace(/0/g, ''): Removes all '0's from the binary string. The operation is O(1) since the string length is at most 32 characters.
 * - .length: Getting the length of the resulting string is O(1).
 * Therefore, the overall time complexity is O(1).
 *
 * Space Complexity: O(1)
 * Reason:
 * - n.toString(2): The binary string representation has a fixed maximum length of 32 characters, which requires O(1) space.
 * - replace(/0/g, ''): The resulting string after removing '0's has a length of at most 32 characters, so it also requires O(1) space.
 * - .length: Retrieving the length of a string does not require additional space.
 * Therefore, the overall space complexity is O(1).
 */
