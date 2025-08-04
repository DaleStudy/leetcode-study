/**
 * @param words: a list of words
 * @return: a string which is correct order
 */
const alienOrder = (words) => {
  const graph = {};

  // 초기화
  for (const word of words) {
    for (const char of word) {
      if (!graph[char]) {
        graph[char] = new Set();
      }
    }
  }

  // 그래프 생성
  for (let i = 1; i < words.length; i++) {
    const prev = words[i - 1];
    const current = words[i];
    let found = false;

    const minLen = Math.min(prev.length, current.length);
    for (let j = 0; j < minLen; j++) {
      if (prev[j] !== current[j]) {
        graph[prev[j]].add(current[j]);
        found = true;
        break;
      }
    }
    // 모순 처리
    if (!found && prev.length > current.length) {
      return '';
    }
  }

  // 탐색
  const output = [];
  const visiting = new Set();
  const visited = new Set();

  function dfs(current) {
    if (visiting.has(current)) {
      return false;
    }
    if (visited.has(current)) {
      return true;
    }

    visiting.add(current);
    for (const adj of graph[current]) {
      if (!dfs(adj)) {
        return false;
      }
    }
    visiting.delete(current);

    visited.add(current);
    output.push(current);
    return true;
  }

  // 순회
  for (const node in graph) {
    if (!dfs(node)) {
      return '';
    }
  }

  return output.reverse().join('');
}


// 방향 그래프로 선행되는 순서를 표현
// 비슷한 문제: https://leetcode.com/problems/course-schedule/description/

// 위상정렬 사용해서 진입차수 기준 정렬하는 방법도 있음
// 너무 어려웠다...
