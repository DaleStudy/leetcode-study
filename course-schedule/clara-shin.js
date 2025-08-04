/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  // 1. 인접 리스트와 진입 차수 배열 초기화
  const graph = new Array(numCourses).fill(null).map(() => []);
  const inDegree = new Array(numCourses).fill(0);

  // 2. 그래프 구성 및 진입 차수 계산
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    inDegree[course]++; // course의 진입 차수 증가
  }

  // 3. 진입 차수가 0인 노드들을 큐에 추가
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }

  // 4. 위상 정렬 수행
  let processedCourses = 0;

  while (queue.length > 0) {
    const current = queue.shift();
    processedCourses++;

    // 현재 노드와 연결된 모든 노드의 진입 차수 감소
    for (const neighbor of graph[current]) {
      inDegree[neighbor]--;

      // 진입 차수가 0이 되면 큐에 추가
      if (inDegree[neighbor] === 0) {
        queue.push(neighbor);
      }
    }
  }

  // 5. 모든 강의를 처리했는지 확인
  return processedCourses === numCourses;
};
