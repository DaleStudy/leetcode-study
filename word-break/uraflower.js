/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = function (s, wordDict) {
    const dp = Array(s.length);
    const dict = new Set(wordDict);

    function recurse(start) {
        if (start === s.length) return true;
        if (dp[start] !== undefined) return dp[start];

        for (let end = start + 1; end <= s.length; end++) {
            const substr = s.slice(start, end);
            if (dict.has(substr) && recurse(end)) {
                dp[start] = true;
                return true;
            }
        }

        dp[start] = false;
        return false;
    }

    return recurse(0);
};

// 시간복잡도: O(n^2) (n: s.length. n번 재귀 & 최대 n번 슬라이싱)
// 공간복잡도: O(n + m) (m: wordDict.length)
