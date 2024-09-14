// 시간복잡도: O(n * m * n)
// 공간복잡도: O(n)
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordChecks = Array.from({length: s.length}).fill(false)
    const dp = [true, ...wordChecks]

    for (let i = 0 ; i <= s.length; i++) {
        for (let j = 0; j < wordDict.length; j++) {
            const dict = wordDict[j]
            const dictLen  = dict.length

            const checkWord = s.slice(i - dictLen, i)
            if (dp[i - dictLen] && checkWord === dict) {
                dp[i] = true
            }
        }
    }

    return dp[dp.length - 1]
};

console.log(wordBreak("leetcode", ["leet","code"]))
