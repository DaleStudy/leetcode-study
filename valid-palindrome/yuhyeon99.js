/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  const regexp = /[^a-z0-9]/g;
  s = s.toLowerCase();
  s = s.replaceAll(regexp, "");
  
  return s === [...s].reverse().join('');
};
