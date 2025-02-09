// n: len(s)
// Time complexity: O(n^2)
// Space complexity: O(n)

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let answer = 0;
  const map = new Map();

  for (let i = 0; i < s.length; i++) {
    const chr = s[i];

    if (map.has(chr)) {
      const temp = map.get(chr);
      for (const [key, value] of map) {
        if (value <= temp) {
          map.delete(key);
        }
      }
    }

    map.set(chr, i);
    answer = Math.max(answer, map.size);
  }

  return answer;
};
