/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict);
    const dp = new Array(s.length + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            const word = s.slice(j, i);
            if (dp[j] && wordSet.has(word)) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[s.length];
};
