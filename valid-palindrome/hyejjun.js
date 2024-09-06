/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let cleanedString = s.toLowerCase().replace(/[^a-z0-9]/g, '');

  let reversedString = cleanedString.split('').reverse().join('');

  return cleanedString === reversedString;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));
console.log(isPalindrome(" "));

/*
시간 복잡도: O(n)
공간 복잡도: O(n)
*/
