/* 
    time complexity : O(n^2k)
    space complexity : O(n + m)
*/

function wordBreak(s: string, wordDict: string[]): boolean {
   const dp: boolean[] = new Array(s.length + 1).fill(false)

   dp[0] = true

   const wordSet = new Set(wordDict)
   for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
        if (dp[j] && wordSet.has(s.substring(j, i))) {
            dp[i] = true
            break
        }
    }
   }
   return dp[s.length]
};
