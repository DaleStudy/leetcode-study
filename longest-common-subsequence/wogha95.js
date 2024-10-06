/**
 * 알고달레 풀이 참고해서 풀었습니다.
 * @see https://www.algodale.com/problems/longest-common-subsequence/
 *
 * DP + 2차원 배열을 이용한 풀이
 * 행은 text1, 열은 text2에 대응하고
 * index는 text의 처음부터 몇개 문자를 사용할건지 의미합니다.
 * 마지막 문자가 동일하다면 dp[index1][index2] = dp[index1 - 1][index2 - 1] + 1
 * 마지막 문자가 다르다면 dp[index1][index2] = Math.max(dp[index1 - 1][index2], dp[index1][index2 - 1])
 *
 * TC: O(T1 * T2)
 * 2차원 배열을 순회
 *
 * SC: O(T1 * T2)
 * 2차원 배열 생성
 *
 * T1: text1.length, T2: text2.length
 */

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  const LENGTH1 = text1.length;
  const LENGTH2 = text2.length;
  const memory = Array.from({ length: LENGTH1 + 1 }, () =>
    Array.from({ length: LENGTH2 + 1 }, () => 0)
  );

  for (let index1 = 1; index1 <= LENGTH1; index1++) {
    for (let index2 = 1; index2 <= LENGTH2; index2++) {
      if (text1[index1 - 1] === text2[index2 - 1]) {
        memory[index1][index2] = memory[index1 - 1][index2 - 1] + 1;
      } else {
        memory[index1][index2] = Math.max(
          memory[index1 - 1][index2],
          memory[index1][index2 - 1]
        );
      }
    }
  }

  return memory[LENGTH1][LENGTH2];
};
