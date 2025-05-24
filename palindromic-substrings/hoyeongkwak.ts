function countSubstrings(s: string): number {
    const sLen = s.length;
    const dp = Array(sLen).fill(null).map(() => Array(sLen).fill(false))
    let cnt = 0

    for (let i = sLen - 1; i >= 0; i--) {
        for (let j = i; j < sLen; j++) {
            if (i === j) {
                dp[i][j] = true
            } else if (j === i + 1) {
                dp[i][j] = (s[i] === s[j])
            } else {
                dp[i][j] = (s[i] === s[j]) && dp[i + 1][j - 1]
            }

            if (dp[i][j]) cnt++
        }
    }
    return cnt
};
