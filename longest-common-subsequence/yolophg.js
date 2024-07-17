// Time Complexity: O(m * n) m : the length of text1, n : the length of text2
// Space Complexity: O(m * n)

var longestCommonSubsequence = function (text1, text2) {
  // a memoization array to store results
  const memo = Array(text1.length)
    .fill(null)
    .map(() => Array(text2.length).fill(null));

  // helper function that uses recursion and memoization
  function lcsHelper(i, j) {
    // if either string is exhausted, return 0
    if (i === text1.length || j === text2.length) {
      return 0;
    }

    // if characters match, move diagonally and add 1 to the result
    if (text1[i] === text2[j]) {
      memo[i][j] = 1 + lcsHelper(i + 1, j + 1);
    } else {
      // if characters don't match, take the maximum result from moving right or down
      memo[i][j] = Math.max(lcsHelper(i + 1, j), lcsHelper(i, j + 1));
    }

    return memo[i][j];
  }

  // start the recursion from the beginning of both strings
  return lcsHelper(0, 0);
};
