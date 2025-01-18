/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

// Time Complexity: O(n * w * m)
// - n is the length of the string s.
// - w is the number of words in the dictionary wordDict.
// - m is the average length of words in wordDict.

// Space Complexity: O(n)
// - The dp array of size n + 1 is the primary contributor to space usage, where n is the length of the string s.
var wordBreak = function (s, wordDict) {
  dp = new Array(s.length + 1).fill(false);
  dp[0] = true;

  // O(n)
  for (let i = 1; i <= s.length; i++) {
    // O(w)
    for (word of wordDict) {
      if (i >= word.length && s.slice(i - word.length, i) === word) {
        // s.slice(i - word.length, i), the slicing operation takes O(m), where m is the length of the word being checked
        dp[i] = dp[i - word.length];
      }

      if (dp[i]) {
        break;
      }
    }
  }

  return dp[s.length];
};


