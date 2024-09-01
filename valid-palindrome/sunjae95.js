/**
 * @description
 * brainstorming:
 * string method + two pointer
 *
 * time complexity: O(n)
 * space complexity: O(n)
 */

var isPalindrome = function (s) {
  const asciiArray = [];

  for (let i = 0; i < s.length; i++) {
    const asciiCode = s[i].toLowerCase().charCodeAt(0);
    const isNumber = asciiCode >= 48 && asciiCode <= 57;
    const isLowerCase = asciiCode >= 97 && asciiCode <= 122;

    if (isNumber || isLowerCase) asciiArray.push(asciiCode);
  }

  const len = asciiArray.length;
  const middleIndex = Math.floor(len);

  for (let i = 0; i < middleIndex; i++) {
    if (asciiArray[i] !== asciiArray[len - i - 1]) return false;
  }

  return true;
};
