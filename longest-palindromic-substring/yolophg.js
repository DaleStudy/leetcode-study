// Time Complexity: O(n^2)
// Space Complexity: O(1)

var longestPalindrome = function (s) {
  let start = 0,
    maxLength = 1;

  // to expand around the center and update the start and maxLength
  function expandAroundCenter(left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }
    // update the start and maxLength if a longer palindrome is found
    if (maxLength < right - left - 1) {
      start = left + 1;
      maxLength = right - left - 1;
    }
  }

  // iterate through each character in the string
  for (let i = 0; i < s.length; i++) {
    // expand around the current character
    expandAroundCenter(i, i);
    // expand around the current and next character
    expandAroundCenter(i, i + 1);
  }

  // return the longest palindromic substring
  return s.substring(start, start + maxLength);
};
