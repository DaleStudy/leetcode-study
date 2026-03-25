/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const result = s.toLowerCase().replace(/[^a-z0-9]/g, '');
  return result === result.split('').reverse().join('');
};
