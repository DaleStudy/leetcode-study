/**
 * 문제 설명
 * - 두 문자열의 가장 긴 공통 부분 문자열의 길이를 반환
 * - 대표적인 DP 문제
 *
 * 아이디어
 * 1) 브루투포스 O(n^2)
 * 2) DP O(n^2)
 *   - dp[i][j]를 만들어서 text1[i]와 text2[j]가 같은 경우 dp[i][j] = dp[i-1][j-1] + 1
 *   - 다른 경우 dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1])
 */

function longestCommonSubsequence(text1: string, text2: string): number {
  const dp = Array.from({ length: text1.length + 1 }, () =>
    Array(text2.length + 1).fill(0)
  );

  for (let i = 1; i <= text1.length; i++) {
    for (let j = 1; j <= text2.length; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[text1.length][text2.length];
}
