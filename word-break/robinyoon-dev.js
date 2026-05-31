// 문풀 해설 보고 푼 문제
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {

    const dp = new Array(s.length + 1).fill(false);
    dp[0] = true;

    let maxLength = 0;
    for (let word of wordDict) {
        maxLength = Math.max(maxLength, word.length);
    }

    for (let i = 1; i <= s.length; i++) {
        for (let j = Math.max(0, i - maxLength); j < i; j++) {
            if (dp[j] && wordDict.includes(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[s.length];
};
