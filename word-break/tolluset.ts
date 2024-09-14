/*
 * TC: O(n^2)
 * SC: O(n)
 * */
function wordBreak(s: string, wordDict: string[]): boolean {
  const n = s.length;
  const wordSet = new Set(wordDict);
  const dp = Array(n + 1).fill(false);

  dp[0] = true;

  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordSet.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[n];
}

const tc1 = wordBreak("leetcode", ["leet", "code"]); // true
console.info("🚀 : tolluset.ts:17: tc1=", tc1);

const tc2 = wordBreak("applepenapple", ["apple", "pen"]); // true
console.info("🚀 : tolluset.ts:20: tc2=", tc2);

const tc3 = wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]); // false
console.info("🚀 : tolluset.ts:23: tc3=", tc3);

const tc4 = wordBreak("cars", ["car", "ca", "rs"]); // true
console.info("🚀 : tolluset.ts:27: tc4=", tc4);

const tc5 = wordBreak("aaaaaaa", ["aaaa", "aaa"]); // true
console.info("🚀 : tolluset.ts:32: tc5=", tc5);

const tc6 = wordBreak("cbca", ["bc", "ca"]); // false
console.info("🚀 : tolluset.ts:43: tc6=", tc6);
