/**
 * TC: O(N^2)
 * 주어진 s 문자열이 한 종류의 문자로 이루어져있다면 for문에서 O(N), while문에서 O(N) 이므로 O(N * 2N)
 *
 * SC: O(1)
 */

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let result = "";

  for (let index = 0; index < s.length; index++) {
    const [start1, end1] = getPalindromicSubstringLength(index, index);
    const [start2, end2] = getPalindromicSubstringLength(index, index + 1);

    if (result.length < end1 - start1 + 1) {
      result = s.substring(start1, end1 + 1);
    }

    if (result.length < end2 - start2 + 1) {
      result = s.substring(start2, end2 + 1);
    }
  }

  return result;

  function getPalindromicSubstringLength(start, end) {
    while (0 <= start && end < s.length && s[start] === s[end]) {
      start -= 1;
      end += 1;
    }

    return [start + 1, end - 1];
  }
};
