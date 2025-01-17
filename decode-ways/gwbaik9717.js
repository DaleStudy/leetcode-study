// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  const n = s.length;
  const dp = Array.from({ length: n + 2 }, () => 0);
  dp[1] = 1;

  for (let i = 2; i < n + 2; i++) {
    // 한자리
    const charCode = Number(s[i - 2]);

    if (charCode > 0) {
      dp[i] += dp[i - 1];
    }

    // 두자리
    if (i <= 2) {
      continue;
    }

    if (Number(s[i - 3]) == 0) {
      continue;
    }

    const strCode = Number(s.slice(i - 3, i - 1));

    if (strCode > 0 && strCode <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp.at(-1);
};
