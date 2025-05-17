/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function (s) {
  let longest = 0;
  let start = 0;
  const seen = {};

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (seen[char] >= start) {
      start = seen[char] + 1;
    }
    seen[char] = i;
    longest = Math.max(longest, i - start + 1);
  }

  return longest;
};
