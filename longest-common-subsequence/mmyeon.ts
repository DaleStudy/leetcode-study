/**
 * @link https://leetcode.com/problems/longest-common-subsequence/description/
 *
 * 접근 방법 :
 * - LCS 길이 담을 DP 배열 선언
 * - 문자 순회하면서 같은 문자인 경우, 이전 값 + 1 로 업데이트
 * - 문자 다른 경우, 이전 값 그대로 유지
 *
 * 시간복잡도 : O(m * n)
 *  - 두 문자열 길이 크기만큼 이중 반복문 실행
 *
 * 공간복잡도 : O(m * n)
 *  - 두 문자 길이 크기만큼 DP 배열에 저장
 */
function longestCommonSubsequence(text1: string, text2: string): number {
  const m = text1.length,
    n = text2.length;

  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[m][n];
}
