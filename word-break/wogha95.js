/**
 * TC: O(W * S)
 * 4번에서 W만큼 순회 * 메모이제이션 S
 *
 * SC: O(S)
 * queue 최대 S + visited 최대 S
 *
 * S: s.length, W: wordDict.length
 */

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const queue = [0];
  const visited = new Set();

  while (queue.length) {
    const start = queue.shift();
    // 1. 도착했다면 정답 반환
    if (start === s.length) {
      return true;
    }
    // 2. 이미 방문한 경우 순회 방지
    if (visited.has(start)) {
      continue;
    }

    // 3. 방문 표시 남기고
    visited.add(start);
    // 4. wordDict의 word를 이용할 있는 경우
    for (const word of wordDict) {
      if (s.slice(start, start + word.length) === word) {
        queue.push(start + word.length);
      }
    }
  }

  return false;
};

/**
 * TC: O(W * S)
 * 2번에서 W만큼 순회 * 메모이제이션 S
 *
 * SC: O(S)
 * possibleS의 길이 S + dfs의 깊이는 최대 S
 *
 * S: s.length, W: wordDict.length
 */

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  // 1. S의 index번째 글자까지 wordDict 조합이 가능한지 표시하는 배열
  const possibleS = new Array(s.length + 1).fill(false);

  dfs(0);

  return possibleS[s.length];

  function dfs(start) {
    // 2. wordDict의 word를 이용할 있는 경우
    for (const word of wordDict) {
      if (s.slice(start, start + word.length) === word) {
        // 3. 이미 조합 가능 표시가 있는 index의 경우 백트래킹
        if (possibleS[start + word.length]) {
          return;
        }

        // 4. 조합 가능하다는 표시를 하고 다음 index로 재귀
        possibleS[start + word.length] = true;
        dfs(start + word.length);
      }
    }
  }
};
