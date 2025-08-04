/**
 * https://leetcode.com/problems/palindromic-substrings/submissions/1644425061/
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  let count = 0;

  // Helper function to expand around the center
  function expandAroundCenter(left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      count++; // Found a palindrome
      left--;
      right++;
    }
  }

  for (let i = 0; i < s.length; i++) {
    expandAroundCenter(i, i); // Odd-length palindromes
    expandAroundCenter(i, i + 1); // Even-length palindromes
  }

  return count;
};
