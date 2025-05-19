// Memoized DFS
// TC: O(m * n)
// SC: O(m * n)
function uniquePaths(m: number, n: number): number {
  const memo = new Map<string, number>();

  const traverse = (row: number, col: number) => {
    if (row >= m || col >= n) return 0;
    if (row === m - 1 && col === n - 1) return 1;
    const key = `${row}-${col}`;
    if (memo.has(key)) return memo.get(key);

    const result = traverse(row + 1, col) + traverse(row, col + 1);
    memo.set(key, result);
    return result;
  };

  return traverse(0, 0);
}

// DP
// TC: O(m * n)
// SC: O(m * n)
/*
function uniquePaths(m: number, n: number): number {

    // 1,     1,      1
    // 1,  1+1=2, 1+(1+1)=3

    const dp = Array.from({length: m}, () => Array(n).fill(1));

    for(let i=1; i<m; i++) {
        for(let j=1; j<n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }

    return dp[m-1][n-1];
};
*/

