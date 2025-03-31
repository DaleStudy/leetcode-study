/**
 * @link https://leetcode.com/problems/course-schedule/description/
 *
 * 접근 방법 :
 *  - 주어진 과목에서 선수 과목 사이클이 존재하는지 확인하기 위해서 dfs 사용
 *  - 사이클이 있다는 건 탐색 중에 다시 동일 과목이 등장한 경우니까, 과목별 결과 저장하기 위해서 visited 배열 사용
 *
 * 시간복잡도 : O(n + e)
 *  - n = 들어야 하는 과목 수
 *  - e = 선수 과목과 연결된 과목 수
 *  - 선수 과목 dfs 호출하고, 선수 과목과 연결된 과목도 호출함
 *
 * 공간복잡도 : O(n + e)
 *  - n = 들어야 하는 과목 수
 *  - e = 선수 과목과 연결된 과목 수
 *  - visited 배열 : O(n)
 *  - Map : O(e)
 */

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  // 선수 과목을 키, 후속 과목을 값으로 저장
  const map = new Map<number, number[]>();

  for (const [course, prerequisite] of prerequisites) {
    if (!map.has(prerequisite)) map.set(prerequisite, []);
    map.get(prerequisite)!.push(course);
  }

  // 이미 탐색중인 과목인지 확인하기 위한 배열
  // 미탐색 : 0, 탐색중: 1, 탐색완료 : 2로 처리
  const visited = Array(numCourses).fill(0);

  const dfs = (course: number) => {
    // 탐색중이면 사이클이 발생
    if (visited[course] === 1) return false;
    // 탐색 완료인 과목은 사이클이 없는 상태니까 true 리턴
    if (visited[course] === 2) return true;

    // 탐색 시작
    // 탐색 중인 상태로 변경
    visited[course] = 1;

    const nextCourses = map.get(course) ?? [];

    // 후속 과목 모두 체크
    for (const nextCourse of nextCourses) {
      if (!dfs(nextCourse)) return false;
    }

    // 탐색 완료 상태로 변경
    visited[course] = 2;
    return true;
  };

  // 들어야 하는 모든 과목에 대해 dfs 호출
  for (let i = 0; i < numCourses; i++) {
    // 미탐색 노드만 탐색하도록 처리
    if (visited[i] === 0 && !dfs(i)) return false;
  }

  return true;
}
