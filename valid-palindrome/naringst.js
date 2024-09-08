/**
 * @param {string} s
 * @return {boolean}
 */

/**
 * Runtime: 66ms, Memory: 54.75MB
 * Time complexity: O(s.length)
 * Space complexity: O(s.length)
 *
 */

var isPalindrome = function (s) {
  let trimmed = s.toLowerCase();
  let answer = [];
  let checkAlphabet = /[a-zA-Z]/;
  let checkNum = /[0-9]/;

  for (let alpha of trimmed) {
    if (checkAlphabet.test(alpha) || checkNum.test(alpha)) {
      answer.push(alpha);
    }
  }

  if (answer.join("") === answer.reverse().join("")) {
    return true;
  }
  return false;
};
