/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */

// 🍎 DP
// Time Complexity: O(m*n)
// Space Complexity: O(n)

// Row 0: [1, 1, 1, 1]
// Row 1: [1, 2, 3, 4]
// Row 2: [1, 3, 6, 10]

// Initial dp: [1, 1, 1, 1]
// left = 1 (always starts with 1 for the first column)

// col = 1: left += dp[1] → left = 1 + 1 = 2 → dp[1] = left
// col = 2: left += dp[2] → left = 2 + 1 = 3 → dp[2] = left
// col = 3: left += dp[3] → left = 3 + 1 = 4 → dp[3] = left

// dp after row 1: [1, 2, 3, 4]

// Initial dp: [1, 2, 3, 4]
// left = 1

// col = 1: left += dp[1] → left = 1 + 2 = 3 → dp[1] = left
// col = 2: left += dp[2] → left = 3 + 3 = 6 → dp[2] = left
// col = 3: left += dp[3] → left = 6 + 4 = 10 → dp[3] = left

// dp after row 2: [1, 3, 6, 10]

var uniquePaths = function (m, n) {
  let dp = new Array(n).fill(1);

  for (let row = 1; row < m; row++) {
    let left = 1;
    for (let col = 1; col < n; col++) {
      left += dp[col];
      dp[col] = left;
    }
  }

  return dp[n - 1];
};

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */

// 🍎 DFS
// Time Complexity: O(m*n)
// Space Complexity: O(m*n)

// var uniquePaths = function (m, n) {
//   const memo = {};

//   const dfs = (row, col) => {
//     if (row === m - 1 && col === n - 1) {
//       return 1;
//     }

//     let cnt = 0;

//     const key = `${row}, ${col}`;
//     if (key in memo) {
//       return memo[key];
//     }

//     if (row + 1 < m) {
//       cnt += dfs(row + 1, col);
//     }

//     if (col + 1 < n) {
//       cnt += dfs(row, col + 1);
//     }

//     memo[key] = cnt;

//     return cnt;
//   };

//   return dfs(0, 0);
// };
