/**
 * @param {string} str
 * @return {number}
 */
var lengthOfLongestSubstring = function (str) {
  let maxLength = 0;
  let left = 0;
  const lastSeenCharIndexMap = {};

  for (let right = 0; right < str.length; right++) {
    const currentChar = str[right];

    // If the current character was seen before, update the left pointer
    if (lastSeenCharIndexMap[currentChar] >= left) {
      left = lastSeenCharIndexMap[currentChar] + 1;
    }

    lastSeenCharIndexMap[currentChar] = right;

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};

/**
 * Time Complexity: O(n)
 * - The right pointer iterates through the string once, making it O(n).
 * - The left pointer only moves when a duplicate character is found, ensuring each character is processed at most twice.
 * - Thus, the total time complexity is O(n).
 *
 * Space Complexity: O(min(n, m))
 * - The space complexity is determined by the size of the character map, which stores the indices of characters in the current window.
 * - In the worst case, the map could store all unique characters in the string.
 * - Thus, the space complexity is O(min(n, m)), where n is the length of the string and m is the character set size.
 */
