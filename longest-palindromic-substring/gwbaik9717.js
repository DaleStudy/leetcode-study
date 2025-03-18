// Time complexity: O(n^2)
// Space complexity: O(n^2)

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  const dp = Array.from({ length: s.length }, () =>
    Array.from({ length: s.length }, () => false)
  );

  let answer = "";
  let start = 0;
  let end = 0;

  const update = (i, j) => {
    const newLen = Math.abs(i - j) + 1;

    if (newLen > end - start + 1) {
      start = i;
      end = j;
    }
  };

  for (let i = s.length - 1; i >= 0; i--) {
    for (let j = i; j < s.length; j++) {
      if (i === j) {
        dp[i][j] = true;
        update(i, j);
        continue;
      }

      if (i + 1 === j) {
        if (s[i] === s[j]) {
          dp[i][j] = true;
          update(i, j);
        }

        continue;
      }

      if (dp[i + 1][j - 1] && s[i] === s[j]) {
        dp[i][j] = true;
        update(i, j);
      }
    }
  }

  return s.slice(start, end + 1);
};
