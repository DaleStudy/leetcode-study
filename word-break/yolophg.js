// Time Complexity: O(n^2 * m) m : the average length of the words in the dictionary
// Space Complexity: O(n)

var wordBreak = function (s, wordDict) {
  const n = s.length;

  // a dp array where dp[i] means s[0..i-1] can be segmented into words
  let dp = Array(n + 1).fill(false);

  // to segment an empty string
  dp[0] = true;

  for (let i = 1; i <= n; i++) {
    // check every substring s[j..i-1]
    for (let j = 0; j < i; j++) {
      // if s[0..j-1] can be segmented and s[j..i-1] is a word
      if (dp[j] && wordDict.includes(s.substring(j, i))) {
        dp[i] = true;
        // no need to check further, we found a valid segmentation
        break;
      }
      ``;
    }
  }

  // whether s[0..n-1] can be segmented
  return dp[n];
};
