/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let maxLength = 0;
  const charSet = new Set();

  let start = 0, end = 0;

  while (end < s.length) {
      if (charSet.has(s[end])) {
          charSet.delete(s[start]);
          start += 1;
          continue;
      }

      charSet.add(s[end]);
      end += 1;
      maxLength = Math.max(maxLength, end - start);
  }

  return maxLength;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
