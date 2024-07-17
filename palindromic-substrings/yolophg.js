// Time Complexity: O(n^2)
// Space Complexity: O(n^2)

var countSubstrings = function (s) {
  const n = s.length;
  // a 2D array to store palindrome information
  let dp = Array.from(Array(n), () => Array(n).fill(false));
  let count = 0;

  // every single character is a palindrome
  for (let i = 0; i < n; i++) {
    dp[i][i] = true;
    count++;
  }

  // check for palindromic substrings of length 2
  for (let i = 0; i < n - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true;
      count++;
    }
  }

  // check for palindromic substrings of length 3 and more
  for (let len = 3; len <= n; len++) {
    for (let i = 0; i < n - len + 1; i++) {
      //eEnding index of the current substring
      let j = i + len - 1;
      if (s[i] === s[j] && dp[i + 1][j - 1]) {
        dp[i][j] = true;
        count++;
      }
    }
  }

  // return the total count
  return count;
};
