/*
    time complexity : O(m * n)
    space complexity : O(m * n)
*/
function uniquePaths(m: number, n: number): number {
    const dp = Array.from({ length: m }, () => Array(n).fill(1)) 
    let results = 0
    for (let r = 1; r < m; r++) {
        for (let c = 1; c < n; c++) {  
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        }
    }
    return dp[m-1][n-1]
};
