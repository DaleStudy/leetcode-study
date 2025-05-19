/*
* 시간 복잡도: O(n)
* 공간 복잡도; O(n)
*
* 과정:
* 1. 소문자, 대문자, 숫자만 파싱
* 2. 소문자로 변환
* 3. 리버스 스트링과 기본 스트링과 대조
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  const parsedString = s.replace(/[^a-zA-Z0-9]/g, '');
  const lowerString = parsedString.toLowerCase();
  const reverseString = lowerString.split("").reverse().join("");
  return reverseString === lowerString;
};
