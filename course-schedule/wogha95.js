/**
 * TC: O(V + E)
 * SC: O(V + E)
 * N: numCourses(all of vertex), P: prerequisites(all of edge)
 */

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const STEP = {
    before: 0,
    ing: 1,
    after: 2,
  };
  const stepBoard = Array.from({ length: numCourses }, () => STEP.before);
  const board = Array.from({ length: numCourses }, () => []);

  for (const [a, b] of prerequisites) {
    board[a].push(b);
  }

  for (let index = 0; index < numCourses; index++) {
    if (isCycle(index)) {
      return false;
    }
  }
  return true;

  function isCycle(current) {
    if (stepBoard[current] === STEP.end) {
      return false;
    }
    if (stepBoard[current] === STEP.ing) {
      return true;
    }

    stepBoard[current] = STEP.ing;
    for (const next of board[current]) {
      if (isCycle(next)) {
        return true;
      }
    }
    stepBoard[current] = STEP.end;
    return false;
  }
};
