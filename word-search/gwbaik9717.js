// h: height of the board, w: width of the board, n: length of the word
// Time complexity: O(h * w * 4**n)
// Space complexity: O(n)

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const n = word.length;
  const h = board.length;
  const w = board[0].length;

  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];

  let answer = false;

  const dfs = (current, index) => {
    if (index === n - 1) {
      answer = true;
      return;
    }

    const [cy, cx] = current;
    const value = board[cy][cx];
    board[cy][cx] = "";

    for (let i = 0; i < dy.length; i++) {
      const ny = cy + dy[i];
      const nx = cx + dx[i];
      const ni = index + 1;

      if (
        ny >= 0 &&
        ny < h &&
        nx >= 0 &&
        nx < w &&
        board[ny][nx] &&
        word[ni] === board[ny][nx]
      ) {
        dfs([ny, nx], ni);
      }
    }

    board[cy][cx] = value;
  };

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (board[i][j] === word[0] && !answer) {
        dfs([i, j], 0);
      }
    }
  }

  return answer;
};
