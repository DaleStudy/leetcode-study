// n: height of matrix, m: width of matrix
// Time complexity: O(n*m)
// Space complexity: O(n+m)

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const n = matrix.length;
  const m = matrix[0].length;

  // order of direction: East, South, West, North
  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];

  let dir = 0;
  let y = 0;
  let x = 0;

  const answer = [];

  while (true) {
    answer.push(matrix[y][x]);
    matrix[y][x] = "";

    let ny = y + dy[dir];
    let nx = x + dx[dir];

    if (ny >= 0 && ny < n && nx >= 0 && nx < m && matrix[ny][nx] !== "") {
      y = ny;
      x = nx;
      continue;
    }

    // If the new position is out of bounds or already visited, Change direction
    dir = (dir + 1) % 4;

    ny = y + dy[dir];
    nx = x + dx[dir];

    // If the changed direction still has a problem, Break the loop
    if (ny < 0 || ny >= n || nx < 0 || nx >= m || matrix[ny][nx] === "") {
      break;
    }

    y = ny;
    x = nx;
  }

  return answer;
};
