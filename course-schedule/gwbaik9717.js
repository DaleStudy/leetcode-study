// n: numCourses, p: len(prerequisites)
// Time complexity: O(n + p)
// Space complexity: O(n + p)

class _Queue {
  constructor() {
    this.q = [];
    this.start = 0;
    this.end = 0;
  }

  isEmpty() {
    return this.start === this.end;
  }

  push(value) {
    this.q.push(value);
    this.end++;
  }

  shift() {
    const rv = this.q[this.start];
    delete this.q[this.start++];

    return rv;
  }
}

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const inDegree = Array.from({ length: numCourses }, () => 0);

  for (const [end, start] of prerequisites) {
    graph[start].push(end);
    inDegree[end]++;
  }

  const q = new _Queue();

  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      q.push(i);
    }
  }

  let count = 0;

  while (!q.isEmpty()) {
    const current = q.shift();
    count++;

    // 현재 노드와 연결된 다른 노드의 차수 감소
    for (const node of graph[current]) {
      inDegree[node] -= 1;

      if (inDegree[node] === 0) {
        q.push(node);
      }
    }
  }

  return count === numCourses;
};
