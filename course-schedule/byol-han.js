/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  if (numCourses === 1) return true; // 과목이 1개면 무조건 수강 가능

  let adjList = new Map(); // 각 과목에 대해 선행 과목들을 저장하는 인접 리스트
  let visited = new Set(); // 이미 수강 가능한 것으로 확인된 과목들
  let path = new Set(); // 현재 DFS 경로에 포함된 과목들 (사이클 확인용)

  // 모든 과목을 인접 리스트에 초기화
  for (let i = 0; i < numCourses; i++) {
    adjList.set(i, []);
  }

  // prerequisite 정보를 기반으로 인접 리스트 구성
  for (let i = 0; i < prerequisites.length; i++) {
    // [0, 1]은 0을 듣기 위해 1을 먼저 들어야 함
    adjList.get(prerequisites[i][0]).push(prerequisites[i][1]);
  }

  // DFS 함수: 해당 course를 수강할 수 있는지 확인
  const canTake = (course) => {
    if (visited.has(course)) return true; // 이미 확인된 코스는 재확인 필요 없음
    if (path.has(course)) return false; // 현재 DFS 경로에 course가 있다면 사이클 발생

    path.add(course); // 현재 경로에 course 추가

    let preCourses = adjList.get(course); // course를 듣기 위한 선행 과목들
    for (let i = 0; i < preCourses.length; i++) {
      if (!canTake(preCourses[i])) return false; // 선행 과목 중 하나라도 불가능하면 종료
    }

    path.delete(course); // 경로에서 제거 (백트래킹)
    visited.add(course); // 수강 가능한 것으로 확인
    return true;
  };

  // 모든 과목에 대해 수강 가능한지 확인
  for (let i = 0; i < numCourses; i++) {
    path = new Set(); // 새로운 DFS 탐색이므로 경로 초기화
    if (!canTake(i)) return false; // 한 과목이라도 못 들으면 false
  }

  return true; // 모든 과목 수강 가능
};
