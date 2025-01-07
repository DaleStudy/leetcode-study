/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

// board(N * M), where N is the number of row and M is the number of columns
// L, the length of the word
// TC : O(N * M * 4^L)

// recursion depth : the length of the word (L)
// each recursion call requires constant space.
// SC : O(L)

var exist = function (board, word) {
  let row = board.length;
  let col = board[0].length;

  const dfs = (r, c, idx) => {
    // search done
    if (idx === word.length) {
      return true;
    }

    // row and column are out of range
    if (r < 0 || r >= row || c < 0 || c >= col) {
      return false;
    }

    if (board[r][c] !== word[idx]) {
      return false;
    }

    // word[idx] === board[r][c]
    // continue searching for word[idx + 1] in adjacent cells on the board
    const temp = board[r][c];
    board[r][c] = "visited";

    const arr = [
      [1, 0], // Move down
      [-1, 0], // Move up
      [0, 1], // Move right
      [0, -1], // Move left
    ];
    for (const [up, right] of arr) {
      if (dfs(r + up, c + right, idx + 1)) {
        return true;
      }
    }

    board[r][c] = temp;
    return false;
  };

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (dfs(i, j, 0)) {
        return true;
      }
    }
  }

  return false;
};



