/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

// ✅ Graph DFS (Depth-First Search) approach
// Time Complexity: O(V + E), where V is the number of courses (numCourses) and E is the number of prerequisites (edges).
// Space Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.

var canFinish = function (numCourses, prerequisites) {
  // prerequisites = [
  // [1, 0], // Course 1 depends on Course 0
  // [2, 1], // Course 2 depends on Course 1
  // [3, 1], // Course 3 depends on Course 1
  // [3, 2]  // Course 3 depends on Course 2
  // ];

  // graph = {
  // 0: [1], // Course 0 is a prerequisite for Course 1
  // 1: [2, 3], // Course 1 is a prerequisite for Courses 2 and 3
  // 2: [3], // Course 2 is a prerequisite for Course 3
  // 3: [] // Course 3 has no prerequisites
  // };

  // Build the graph
  const graph = {};

  // for(let i=0; i<numCourses; i++) {
  //     graph[i] = []
  // }

  // Fill in the graph with prerequisites
  for (const [course, prereq] of prerequisites) {
    if (!graph[prereq]) {
      graph[prereq] = [];
    }
    graph[prereq].push(course);
  }

  const visited = new Array(numCourses).fill(0);

  const dfs = (course) => {
    if (visited[course] === 1) return false; // cycle detected!
    if (visited[course] === 2) return true; // already visited

    visited[course] = 1;

    // // Visit all the courses that depend on the current course
    for (const nextCourse of graph[course] || []) {
      if (!dfs(nextCourse)) {
        return false; // cycle detected!
      }
    }

    visited[course] = 2; // fully visited and return true
    return true;
  };

  // Check for each course whether it's possible to finish it
  for (let i = 0; i < numCourses; i++) {
    if (!dfs(i)) {
      return false; // cycle detected!
    }
  }

  return true; // no cycles
};

