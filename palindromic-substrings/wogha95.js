// TC: O(n^3)
// SC: O(1)

/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
  let count = 0;

  for (let left = 0; left < s.length; left++) {
      for (let right = left; right < s.length; right++) {
          if(checkIsPalinDrome(left, right)) {
              count += 1;
          }
      }
  }

  return count;

  function checkIsPalinDrome(left, right) {
      while (left < right) {
          if (s[left] !== s[right]) {
              return false;
          }
          left += 1;
          right -= 1;
      }

      return true;
  }
};
