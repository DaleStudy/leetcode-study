/**
 * 문제 유형
 * - DP (점화식 이용, 백트래킹 사용시 TLE 발생)
 *
 * 문제 설명
 * - 주어진 문자열을 숫자로 변환하는 방법의 갯수를 구하는 문제
 *
 * 아이디어
 * 1) f(i) = 마지막 한자리수가 변환 가능하면 f(i-1) + 마지막 두자리수가 가능하면 f(i-2)
 *   - 한자리수는 0만 아니면 됨, 두자리수는 10~26 사이여야 함.
 *
 */
function numDecodings(s: string): number {
  const n = s.length;
  if (n === 1) return s[0] === "0" ? 0 : 1;

  const dp = Array(n + 1).fill(0);
  dp[0] = 1;
  dp[1] = s[0] === "0" ? 0 : 1;

  for (let i = 2; i <= n; i++) {
    const one = Number(s[i - 1]);
    const two = Number(s[i - 2] + s[i - 1]);
    if (one !== 0) dp[i] += dp[i - 1];
    if (two >= 10 && two <= 26) dp[i] += dp[i - 2];
  }

  return dp[n];
}
