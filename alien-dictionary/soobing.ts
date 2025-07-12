/**
 * 문제 설명
 * - 주어진 단어들을 활용하여 알파벳 순서를 찾는 문제
 *
 * 아이디어
 * 1) 위상정렬 (👀 다음에 다시풀어보기) - Kahn's Algorithm
 *   - 어렵다...
 */
function alienOrder(words: string[]): string {
  const graph: Map<string, Set<string>> = new Map();
  const inDegree: Map<string, number> = new Map(); // 간선의 갯수(첫 시작이 무엇인지 판단하기 위함)

  // 단어들에 나오는 모든 문자를 정리 및 초기화
  for (const word of words) {
    for (const char of word) {
      if (!graph.has(char)) {
        graph.set(char, new Set());
        inDegree.set(char, 0);
      }
    }
  }

  // 단어들을 비교해서 알파벳 간의 우선 순서(그래프의 간선) 추출
  for (let i = 0; i < words.length - 1; i++) {
    const w1 = words[i];
    const w2 = words[i + 1];
    const minLen = Math.min(w1.length, w2.length);

    let foundDiff = false;

    for (let j = 0; j < minLen; j++) {
      const c1 = w1[j];
      const c2 = w2[j];
      if (c1 !== c2) {
        if (!graph.get(c1)!.has(c2)) {
          graph.get(c1)!.add(c2);
          inDegree.set(c2, inDegree.get(c2)! + 1);
        }
        foundDiff = true;
        break;
      }
    }

    // 사전순이 아닌 경우 빈문자열 리턴(If the order is invalid, return an empty string.)
    if (!foundDiff && w1.length > w2.length) return "";
  }

  // BFS 위상정렬 시작
  const queue: string[] = [];
  for (const [char, degree] of inDegree.entries()) {
    if (degree === 0) queue.push(char);
  }

  const result: string[] = [];
  while (queue.length > 0) {
    const current = queue.shift()!;
    result.push(current);

    for (const neighbor of graph.get(current)!) {
      inDegree.set(neighbor, inDegree.get(neighbor)! - 1);
      if (inDegree.get(neighbor) === 0) {
        queue.push(neighbor);
      }
    }
  }

  return result.length === inDegree.size ? result.join("") : "";
}
