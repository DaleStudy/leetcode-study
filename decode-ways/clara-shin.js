/**
 * 숫자 문자열이 주어졌을 때, 이를 알파벳으로 해독할 수 있는 방법의 수를 구하기
 *
 * 다이나믹 프로그래밍(DP)
 * (1)각 위치에서 시작하여 문자열을 해독하는 방법의 수를 계산
 * (2)중복 계산을 피하기 위해 DP를 사용
 */

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (s.length === 0 || s[0] === '0') return 0;

  const dp = new Array(s.length + 1).fill(0);

  dp[0] = 1;
  dp[1] = s[0] !== '0' ? 1 : 0;

  for (let i = 2; i <= s.length; i++) {
    // 한 자리 숫자로 해독하는 경우 (현재 숫자가 1-9)
    if (s[i - 1] !== '0') {
      dp[i] += dp[i - 1];
    }

    // 두 자리 숫자로 해독하는 경우 (10-26)
    const twoDigit = parseInt(s.substring(i - 2, i));
    if (twoDigit >= 10 && twoDigit <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[s.length];
};
