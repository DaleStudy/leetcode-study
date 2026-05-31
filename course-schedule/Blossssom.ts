/**
 * @pseudocode
 * - 선행 수업에 대해 Map으로 정리
 *
 * - numCoureses 만큼의 반복 시작
 *  - 탐색 시작
 *  - 만약 방문 중인 상태 : true
 *  - 만약 이미 방문한 상태 : false
 *  - 현재 탐색한 값을 visit에 저장
 *  - Map에 정리된 다음 수업 탐색
 *
 *
 * @param numCourses
 * @param prerequisites
 * @returns
 */

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const obj: Record<number, number[]> = prerequisites.reduce(
    (acc: Record<number, number[]>, cur: number[]) => {
      const [a, b] = cur;
      acc[a] ? (acc[a] = [...acc[a], b]) : (acc[a] = [b]);
      return acc;
    },
    {}
  );

  const visited = Array.from({ length: numCourses }, () => 0);

  function hasCycle(current: number): boolean {
    if (obj[current] === undefined) {
      return false;
    }
    // 방문 중
    if (visited[current] === 1) {
      return true;
    }

    // 방문 완료
    if (visited[current] === 2) {
      return false;
    }

    visited[current] = 1;

    for (const next of obj[current]) {
      if (hasCycle(next)) {
        return true;
      }
    }

    visited[current] = 2;
    return false;
  }

  for (let i = 0; i < numCourses; i++) {
    if (hasCycle(i)) {
      return false;
    }
  }
  return true;
}

const numCourses = 2;
const prerequisites = [
  [1, 0],
  [0, 1],
];

canFinish(numCourses, prerequisites);



