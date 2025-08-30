/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const cleaned = s.replace(/[^a-z0-9]/gi, "").toLowerCase();

  let left = 0;
  let right = cleaned.length - 1;

  while (left < right) {
    if (cleaned[left] !== cleaned[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};
