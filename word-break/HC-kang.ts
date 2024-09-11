/**
 * https://leetcode.com/problems/word-break
 * T.C. O(s^2)
 * S.C. O(s + w)
 */
function wordBreak(s: string, wordDict: string[]): boolean {
  const wordSet = new Set(wordDict);

  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (!dp[j]) continue;
      if (j-i > 20) break;
      if (wordSet.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[s.length];
}
