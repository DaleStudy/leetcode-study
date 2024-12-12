// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const normalized = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  const reversed = normalized.split("").reverse().join("");

  return normalized === reversed;
};
