/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict); // 빠른 검색을 위한 Set
    const dp = Array(s.length + 1).fill(false);
    dp[0] = true; // 빈 문자열은 항상 가능

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            const word = s.slice(j, i);
            if (dp[j] && wordSet.has(word)) {
                dp[i] = true;
                break; // 더 이상 볼 필요 없음
            }
        }
    }

    return dp[s.length];
};
