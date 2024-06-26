// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

// initialize an array to keep track of the in-degrees for each course
let inDegree = new Array(numCourses).fill(0);
// initialize an adjacency list to represent the graph of courses
let adjList = new Array(numCourses).fill(0).map(() => []);

// fill the in-degree array and adjacency list based on the prerequisites
for (let [course, prereq] of prerequisites) {
  // increment the in-degree of the course
  inDegree[course]++;
  // add the course to the adjacency list of the prerequisite
  adjList[prereq].push(course);
}

// initialize a queue to keep track of courses with no prerequisites (in-degree of 0)
let queue = [];
for (let i = 0; i < numCourses; i++) {
  if (inDegree[i] === 0) {
    queue.push(i);
  }
}

// initialize a counter to keep track of the number of courses that have been processed
let count = 0;

// process the courses with no prerequisites
while (queue.length > 0) {
  // get a course from the queue
  let current = queue.shift();
  // increment the counter as this course can be taken
  count++;

  // iterate through the adjacency list of the current course
  for (let neighbor of adjList[current]) {
    // decrement the in-degree of the neighboring course
    inDegree[neighbor]--;
    // if in-degree becomes 0, add it to the queue
    if (inDegree[neighbor] === 0) {
      queue.push(neighbor);
    }
  }
}

// if the count of processed courses equals the total number of courses, return true
return count === numCourses;
