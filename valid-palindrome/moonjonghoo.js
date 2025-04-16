/**
 * @param {string} s
 * @return {boolean}
 */

var isPalindrome = function (s) {
  // 1. 영숫자만 남기고, 소문자로 변환
  let cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");

  // 2. 뒤집기
  let reversed = cleaned.split("").reverse().join("");

  // 3. 비교
  return cleaned === reversed;
};

isPalindrome("A man, a plan, a canal: Panama");
