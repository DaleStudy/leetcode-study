/**
 * @param {string} s
 * @return {number}
 */

var countSubstrings = function(s) {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
      let start = i;
      let end = i;
      while (start >= 0 && end < s.length && s[start] === s[end]) {
          count += 1;
          start -= 1;
          end += 1;
      }

      start = i;
      end = i + 1;
      while (start >= 0 && end < s.length && s[start] === s[end]) {
          count += 1;
          start -= 1;
          end += 1;
      }
  }

  return count;
};

// 시간 복잡도: O(n^2)
// 공간 복잡도: O(1)
