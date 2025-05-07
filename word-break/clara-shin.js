/**
 * 문자열 s가 주어진 단어 사전 wordDict의 단어들로 분리될 수 있는지 확인하는 문제
 * 다이나믹 프로그래밍(DP)
 * 시간 복잡도: O(n * k) (k: 최대 단어 길이)
 * 공간 복잡도: O(n) (DP 배열 + 단어 집합)
 */

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const n = s.length;
  const dp = new Array(n + 1).fill(false); // DP 배열 초기화
  dp[0] = true; // 빈 문자열은 항상 분리 가능

  const wordSet = new Set(wordDict); // 단어 사전을 Set으로 변환: 검색시간 O(1)

  const maxWordLength = Math.max(...wordDict.map((word) => word.length)); // 단어의 최대 길이 찾기

  for (let i = 0; i <= n; i++) {
    // 가능한 단어 길이만 검사
    for (let j = Math.max(0, i - maxWordLength); j < i; j++) {
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        // dp[j]가 true이고, j부터 i까지의 부분 문자열이 단어 사전에 존재하는 경우
        dp[i] = true;
        break;
      }
    }
  }

  return dp[n];
};
