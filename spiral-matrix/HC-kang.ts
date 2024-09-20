/**
 * https://leetcode.com/problems/spiral-matrix
 * T.C. O(m * n)
 * S.C. O(m * n)
 */
function spiralOrder(matrix: number[][]): number[] {
  const clockwise = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let currentDirection = 0;

  const visited = new Array(matrix.length)
    .fill(0)
    .map(() => new Array(matrix[0].length).fill(false));

  const result: number[] = [];

  let row = 0;
  let col = 0;

  while (result.length < matrix.length * matrix[0].length) {
    result.push(matrix[row][col]);
    visited[row][col] = true;

    const nextRow = row + clockwise[currentDirection][0];
    const nextCol = col + clockwise[currentDirection][1];

    if (
      nextRow < 0 || nextRow >= matrix.length ||
      nextCol < 0 || nextCol >= matrix[0].length ||
      visited[nextRow][nextCol]
    ) {
      currentDirection = (currentDirection + 1) % 4;
    }

    row += clockwise[currentDirection][0];
    col += clockwise[currentDirection][1];
  }

  return result;
}
