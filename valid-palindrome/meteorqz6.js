// 시간 복잡도: O(n)
// 공간 복잡도: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const str = s.toLowerCase();
  let answer = "";
  for (let i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) >= 97 && str.charCodeAt(i) <= 122) {
      answer += str[i];
    } else if (str.charCodeAt(i) >= 48 && str.charCodeAt(i) <= 57) {
      answer += str[i];
    }
  }
  const reversedText = answer.split("").reverse().join("");
  return answer === reversedText;
};
