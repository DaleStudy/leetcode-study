/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (!s || s[0] === "0") return 0;

  const n = s.length;
  const dp = Array(n + 1).fill(0);

  dp[0] = 1; // 빈 문자열은 1가지 방법
  dp[1] = 1; // 첫 글자가 0이 아니면 1가지 방법

  for (let i = 2; i <= n; i++) {
    const oneDigit = parseInt(s.slice(i - 1, i));
    const twoDigits = parseInt(s.slice(i - 2, i));

    if (oneDigit >= 1 && oneDigit <= 9) {
      dp[i] += dp[i - 1];
    }
    if (twoDigits >= 10 && twoDigits <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[n];
};
