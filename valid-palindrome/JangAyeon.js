/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const sLowered = [...s.toLowerCase().replace(" ", "")];
  const isAlpha = (item) => item.charCodeAt() >= 97 && item.charCodeAt() <= 122;
  const isNumber = (item) => item.charCodeAt() >= 48 && item.charCodeAt() <= 57;
  const str = sLowered.filter((c) => isAlpha(c) || isNumber(c));
  const N = str.length;
  let [start, end] = [0, N - 1];
  while (start <= end) {
    if (str[start] != str[end]) {
      return false;
    }
    start++;
    end--;
  }
  return true;
};
