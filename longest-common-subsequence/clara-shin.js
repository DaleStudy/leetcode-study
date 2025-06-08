/**
 * 두 문자열에서 공통으로 나타나는 부분 수열 중 가장 긴 것의 길이를 찾는 문제
 *
 * 다이나믹 프로그래밍(DP): 작은 문제의 결과를 저장해서 큰 문제를 해결하는 방법
 * 시간 복잡도: O(m × n)
 * 공간복잡도: O(min(m, n))
 */
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  // 더 짧은 문자열을 text2로 만들어 공간 절약
  if (text1.length < text2.length) {
    [text1, text2] = [text2, text1];
  }

  const m = text1.length;
  const n = text2.length;

  // 1차원 배열 2개만 사용 (이전 행, 현재 행)
  let prev = Array(n + 1).fill(0);
  let curr = Array(n + 1).fill(0);

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        curr[j] = prev[j - 1] + 1;
      } else {
        curr[j] = Math.max(prev[j], curr[j - 1]);
      }
    }
    // 다음 반복을 위해 배열 교체
    [prev, curr] = [curr, prev];
    curr.fill(0);
  }

  return prev[n];
};
