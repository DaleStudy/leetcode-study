/**
 * @param {string} s
 * @return {number}
 */

function check(str) {
  if (str.length == 2) {
    if (str[0] == '0') return false;
  }
  if (str >= 1 && str <= 26) return true;
  return false;
}

var numDecodings = function (s) {
  if (s[0] == '0') return 0;
  const dp = [1, 1];

  for (let i = 2; i <= s.length; i++) {
    let tmp = dp[i - 1] + dp[i - 2];

    // 2글자 체크 -> dp[i-2]을 뺴줌
    const two_c = String(s[i - 2]) + String(s[i - 1]);
    if (!check(two_c)) tmp -= dp[i - 2];

    // 1글자 체크 -> dp[i-1]을 빼줌
    if (!check(s[i - 1])) tmp -= dp[i - 1];

    if (tmp == 0) return 0;
    dp[i] = tmp;
  }
  return dp[s.length];
};
