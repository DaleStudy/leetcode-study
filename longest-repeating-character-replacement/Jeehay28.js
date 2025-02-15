/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */

// sliding window technique
// Time complexity: O(n), where n is the length of the string. Both the start and end pointers traverse the string at most once.
// Space Complexity: O(1), as we only need a fixed amount of extra space for the character frequency map and some variables.
var characterReplacement = function (s, k) {
  let longest = 0;
  let maxCount = 0;
  const charCount = {};
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    const char = s[end];
    charCount[char] = (charCount[char] || 0) + 1;
    maxCount = Math.max(charCount[char], maxCount);

    while (end - start + 1 - maxCount > k) {
      const temp = s[start];
      charCount[temp] -= 1;
      start += 1;
    }

    longest = Math.max(longest, end - start + 1);
  }

  return longest;
};

