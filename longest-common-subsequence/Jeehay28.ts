// TC: O(m * n)
// SC: O(m * n)
function longestCommonSubsequence(text1: string, text2: string): number {
  const memo = new Map<string, number>();

  const dfs = (i: number, j: number) => {
    const key = `${i}-${j}`;

    if (memo.has(key)) return memo.get(key);

    if (i === text1.length || j === text2.length) {
      // ""
      memo.set(key, 0);
    } else if (text1[i] === text2[j]) {
      memo.set(key, 1 + dfs(i + 1, j + 1)!);
    } else {
      memo.set(key, Math.max(dfs(i + 1, j)!, dfs(i, j + 1)!));
    }

    return memo.get(key);
  };

  return dfs(0, 0)!;
}


// TC: O(m * n)
// SC: O(m * n)
// function longestCommonSubsequence(text1: string, text2: string): number {
//   const m = text1.length + 1;
//   const n = text2.length + 1;

//   const dp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

//   for (let i = 1; i < m; i++) {
//     for (let j = 1; j < n; j++) {
//       // Note: text1[i - 1] and text2[j - 1] because dp uses 1-based indexing,
//       // while the strings use 0-based indexing
//       if (text1[i - 1] === text2[j - 1]) {
//         dp[i][j] = 1 + dp[i - 1][j - 1];
//       } else {
//         dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
//       }
//     }
//   }

//   return dp[m - 1][n - 1];
// }

