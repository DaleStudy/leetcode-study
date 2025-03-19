// ✅ Time Complexity: O(n^2), where n represents the length of the input string s
// ✅ Space Complexity: O(n)

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let max_left = 0,
    max_right = 0;

  for (let i = 0; i < s.length; i++) {
    // Odd-length palindromes
    let left = i,
      right = i;

    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (max_right - max_left < right - left) {
        max_right = right;
        max_left = left;
      }
      left -= 1;
      right += 1;
    }

    // Even-length palindromes
    left = i;
    right = i + 1;

    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (max_right - max_left < right - left) {
        max_right = right;
        max_left = left;
      }
      left -= 1;
      right += 1;
    }
  }

  return s.slice(max_left, max_right + 1);
};

// ✅ Time Complexity: O(n^3), where n represents the length of the input string s
// ✅ Space Complexity: O(n)

/**
 * @param {string} s
 * @return {string}
 */
// var longestPalindrome = function (s) {
//   const isPalindromic = (left, right) => {
//     while (left < right) {
//       if (s[left] !== s[right]) {
//         return false;
//       }
//       left += 1;
//       right -= 1;
//     }

//     return true;
//   };

//   let max_left = 0,
//     max_right = 0;
//   for (let l = 0; l < s.length; l++) {
//     for (let r = 0; r < s.length; r++) {
//       if (isPalindromic(l, r) && max_right - max_left < r - l) {
//         max_left = l;
//         max_right = r;
//       }
//     }
//   }

//   return s.slice(max_left, max_right + 1);
// };

