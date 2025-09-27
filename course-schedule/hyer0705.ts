function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const graph: number[][] = Array.from({ length: numCourses }, () => []);
  const inDegree: number[] = Array(numCourses).fill(0);

  for (const [course, prerequisite] of prerequisites) {
    graph[prerequisite].push(course);
    inDegree[course]++;
  }

  // 지금 당장 수강할 수 있는 과목 목록
  const queue: number[] = [];

  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }

  const result: number[] = [];
  while (queue.length > 0) {
    const course = queue.shift()!;
    result.push(course);

    for (const nextCourse of graph[course]) {
      inDegree[nextCourse]--;
      if (inDegree[nextCourse] === 0) {
        queue.push(nextCourse);
      }
    }
  }

  if (result.length !== numCourses) return false;
  return true;
}
