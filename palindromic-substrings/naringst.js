/**
 * @param {string} s
 * @return {number}
 */

/**
 * Runtime: 1521ms, Memory: 56.61MB
 *
 * Time complexity: O(N^2)
 * Space complexity: O(N^2)
 *
 * Note: necessary to think of an alternative approach
 * **/

function isPalindrome(subString) {
  const len = subString.length;
  for (let i = 0; i < len / 2; i++) {
    if (subString[i] !== subString[len - 1 - i]) {
      return false;
    }
    return true;
  }
}

var countSubstrings = function (s) {
  const n = s.length;
  let answer = n;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let subString = s.slice(i, j + 1);
      if (isPalindrome(subString)) {
        answer += 1;
      }
    }
  }

  return answer;
};
