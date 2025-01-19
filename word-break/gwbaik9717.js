// n: len(s), m: len(wordDict)
// Time complexity: O(n^2*m)
// Space complexity: O(n)

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const dp = Array.from({ length: s.length + 1 }, () => false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (const word of wordDict) {
      const sliced = s.slice(i - word.length, i);

      if (word === sliced && !dp[i]) {
        dp[i] = dp[i - word.length];
      }
    }
  }

  return dp.at(-1);
};
