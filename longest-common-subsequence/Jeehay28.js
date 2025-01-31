/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */

// 🤔
// Both memoization (top-down) and dynamic programming (bottom-up) have the same time and space complexity of O(m * n). 
// The difference lies in their implementation:
// - Memoization uses recursion with a cache to avoid redundant calculations but may incur overhead from recursive calls and stack space.
// - Dynamic Programming iteratively builds the solution, avoiding recursion overhead and sometimes offering better performance.
// DP is often preferred when recursion depth or function call overhead is a concern, while memoization can be more intuitive for certain problems.

// 😊 memoization approach
// Time Complexity: O(m * n), where m is the length of text1, and n is the length of text2
// Space Complexity: O(m * n)
// Top-down approach with recursion.
// Use a cache (or memoization) to store intermediate results.

var longestCommonSubsequence = function (text1, text2) {
  const memo = new Map();

  const dfs = (i, j) => {
    const key = `${i},${j}`; // Convert (i, j) into a unique string key
    if (memo.has(key)) {
      return memo.get(key);
    }

    if (i === text1.length || j === text2.length) {
      memo.set(key, 0);
    } else if (text1[i] === text2[j]) {
      memo.set(key, 1 + dfs(i + 1, j + 1));
    } else {
      memo.set(key, Math.max(dfs(i + 1, j), dfs(i, j + 1)));
    }

    return memo.get(key);
  };
  return dfs(0, 0);
};

// 😊 bottom-up dynamic programming approach
// Time Complexity: O(m * n), where m is the length of text1, and n is the length of text2
// Space Complexity: O(m * n)

// text1 = "abcde"
// text2 = "ace"

//      ""   a   c   e
// ""   0    0   0   0
// a    0    1   1   1
// b    0    1   1   1
// c    0    1   2   2
// d    0    1   2   2
// e    0    1   2   3


// var longestCommonSubsequence = function (text1, text2) {
//     const dp = new Array(text1.length + 1)
//       .fill(0)
//       .map(() => new Array(text2.length + 1).fill(0));
  
//     for (let i = 1; i <= text1.length; i++) {
//       for (let j = 1; j <= text2.length; j++) {
//         if (text1[i - 1] === text2[j - 1]) {
//           dp[i][j] = dp[i - 1][j - 1] + 1;
//         } else {
//           dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
//         }
//       }
//     }
  
//     return dp[text1.length][text2.length];
//   };


// 😱 Time Limit Exceeded!
// Brute-force Recursion
// Time Complexity: O(2^(m+n)) (Exponential)
// Space Complexity: O(m + n) (Recursive Stack)

// var longestCommonSubsequence = function (text1, text2) {
//   const dfs = (i, j) => {
//     if (i === text1.length || j === text2.length) {
//       return 0;
//     }
//     if (text1[i] === text2[j]) {
//       return 1 + dfs(i + 1, j + 1);
//     }
//     return Math.max(dfs(i + 1, j), dfs(i, j + 1));
//   };
//   return dfs(0, 0);
// };


