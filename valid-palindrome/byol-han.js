/**
 * @param {string} s
 * @return {boolean}
 */

// 1. Two Pointers
// time complexity: O(n)
// space complexity: O(1)
var isPalindrome = function (s) {
  let sRefine = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  let left = 0;
  let right = sRefine.length - 1;

  while (left < right) {
    if (sRefine[left] !== sRefine[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};

// 2. String Manipulation
// time complexity: O(n)
// space complexity: O(n)
var isPalindrome = function (s) {
  let refined = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  let reversed = refined.split("").reverse().join("");
  return refined === reversed;
};
