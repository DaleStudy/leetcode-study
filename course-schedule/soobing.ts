/**
 * 문제 해설
 * - 그래프에 사이클이 있는지 없는지 확인하는 문제
 *
 * 아이디어
 * 1) 그래프 탐색 -> DFS, BFS
 * - 그래프를 탐색하며 사이클이 있는지 없는지 확인한다.
 * - 현재 경로에 이미 방문한 노드를 다시 만나면 사이클 발생. = 1
 */

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const graph = new Map<number, number[]>();
  const visited: number[] = new Array(numCourses).fill(0); // 0: 안 다녀옴, 1: 사이클 확인 증(방문 중), 2: 사이클 없음 확인 완료

  // 그래프 생성
  for (const [course, preCourse] of prerequisites) {
    if (!graph.has(course)) graph.set(course, []);
    graph.get(course)!.push(preCourse);
  }

  function hasCycle(index: number) {
    if (visited[index] === 1) return true;
    if (visited[index] === 2) return false;

    visited[index] = 1;
    for (const preCourse of graph.get(index) || []) {
      if (hasCycle(preCourse)) return true;
    }
    visited[index] = 2;
    return false;
  }

  for (let i = 0; i < numCourses; i++) {
    if (hasCycle(i)) return false;
  }
  return true;
}
