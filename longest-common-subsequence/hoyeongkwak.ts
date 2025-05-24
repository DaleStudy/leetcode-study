function longestCommonSubsequence(text1: string, text2: string): number {
    const m1 = text1.length
    const m2 = text2.length
    
    const dp: number[][] = Array(m1 + 1).fill(null).map(() => Array(m2 + 1).fill(0))

    for (let r = 1; r <= m1; r++) {
        for (let c = 1; c <= m2; c++) {
            if (text1[r - 1] === text2[c - 1]) {
                dp[r][c] = dp[r - 1][c - 1] + 1
            } else {
                dp[r][c] = Math.max(dp[r - 1][c], dp[r][c - 1])
            }
        }
    }
    return dp[m1][m2]
};
