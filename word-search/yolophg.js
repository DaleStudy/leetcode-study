// Time Complexity: O(rows×cols)
// Space Complexity: O(rows×cols)

var exist = function (board, word) {
  const rows = board.length;
  const cols = board[0].length;

  // initialize a queue for BFS, starting from each cell in the board
  const queue = [];

  // perform BFS from each cell in the board
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === word[0]) {
        queue.push([[i, j], 0, [[i, j]]]);
      }
    }
  }

  // directions for BFS: up, down, left, right
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  while (queue.length > 0) {
    const [[row, col], index, path] = queue.shift();

    // if the entire word is found, return true
    if (index === word.length - 1) {
      return true;
    }

    // explore neighbors
    for (const [dx, dy] of directions) {
      const newRow = row + dx;
      const newCol = col + dy;

      // check boundaries and character match
      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        board[newRow][newCol] === word[index + 1] &&
        !path.some(([r, c]) => r === newRow && c === newCol)
      ) {
        // enqueue the next cell to explore
        queue.push([[newRow, newCol], index + 1, [...path, [newRow, newCol]]]);
      }
    }
  }

  // if no path was found, return false
  return false;
};
