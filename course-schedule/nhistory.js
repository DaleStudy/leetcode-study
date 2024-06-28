/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  // Initialize in-degree array and graph map
  const inDegree = Array(numCourses).fill(0);
  const graph = new Map();

  // Build the graph and compute in-degrees
  prerequisites.forEach(([course, pre]) => {
    inDegree[course]++;
    if (!graph.has(pre)) {
      graph.set(pre, []);
    }
    graph.get(pre).push(course);
  });

  // Queue for courses with no prerequisites
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }

  // Process the courses
  let count = 0;
  while (queue.length > 0) {
    const course = queue.shift();
    count++;
    if (graph.has(course)) {
      graph.get(course).forEach((nextCourse) => {
        inDegree[nextCourse]--;
        if (inDegree[nextCourse] === 0) {
          queue.push(nextCourse);
        }
      });
    }
  }

  // Return true if all courses can be finished
  return count === numCourses;
};

// TC: O(V + E)
// V is the number of courses, E is the number of prerequisites.
// SC: O(V + E)
