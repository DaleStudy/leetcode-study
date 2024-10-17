/**
 * https://leetcode.com/problems/course-schedule/
 * T.C. O(V + E)
 * S.C. O(V + E)
 */
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const graph: number[][] = Array.from({ length: numCourses }, () => []);
  for (const [course, pre] of prerequisites) {
    graph[pre].push(course);
  }

  const visited = new Array(numCourses).fill(false);
  const visiting = new Array(numCourses).fill(false);

  const dfs = (course: number): boolean => {
    if (visited[course]) return true;
    if (visiting[course]) return false;

    visiting[course] = true;
    for (const neighbor of graph[course]) {
      if (!dfs(neighbor)) return false;
    }
    visiting[course] = false;
    visited[course] = true;

    return true;
  };

  for (let i = 0; i < numCourses; i++) {
    if (!visited[i] && !dfs(i)) return false;
  }

  return true;
}
