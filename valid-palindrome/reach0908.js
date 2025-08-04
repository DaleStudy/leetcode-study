/**
 * 시간복잡도: O(N)
 * 공간복잡도: O(N)
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function (s) {
  const parsedString = s
    .trim()
    .replace(" ", "")
    .replace(/[^a-zA-Z0-9]/g, "")
    .toLowerCase();

  let left = 0;
  let right = parsedString.length - 1;

  while (left < right) {
    if (parsedString[left] !== parsedString[right]) {
      return false;
    }

    left += 1;
    right -= 1;
  }

  return true;
};
