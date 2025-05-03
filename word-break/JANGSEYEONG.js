/**
 * 문자열이 단어 사전 내의 단어들로 분할 가능한지 확인
 *
 * 시간복잡도: O(n * m * k)
 * - n: 문자열 길이
 * - m: 단어 사전 크기
 * - k: 단어 사전 내 가장 긴 단어의 길이
 *
 * 공간복잡도: O(n)
 * - n: 문자열 길이 (메모이제이션 저장 공간)
 *
 * @param {string} s - 분할하려는 문자열
 * @param {string[]} wordDict - 단어 사전
 * @return {boolean} - 문자열을 단어 사전 내 단어들로 분할 가능한지 여부
 */
var wordBreak = function (s, wordDict) {
  // 메모이제이션을 위한 객체
  const memo = {};

  const dfs = function (start) {
    // 이미 계산한 위치라면 저장된 결과 반환
    if (start in memo) return memo[start];

    // 문자열 끝까지 도달했다면 성공
    if (start === s.length) {
      memo[start] = true;
      return true;
    }

    // 모든 단어를 시도
    for (const word of wordDict) {
      // 현재 위치에서 시작하는 부분 문자열이 단어와 일치하는지 확인
      if (s.substring(start, start + word.length) === word) {
        // 남은 문자열도 분할 가능한지 재귀적으로 확인
        if (dfs(start + word.length)) {
          memo[start] = true;
          return true;
        }
      }
    }

    // 현재 위치에서 가능한 분할이 없음
    memo[start] = false;
    return false;
  };

  return dfs(0);
};
