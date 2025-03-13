// n: length of words, k: length of word, h: height of board, w: width of board
// Time complexity: O(4^k * h * w * n)
// Space complexity: O(4^k)

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
  const h = board.length;
  const w = board[0].length;

  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];
  const checked = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => false)
  );

  const findWord = (current, i, word) => {
    const [cy, cx] = current;

    if (i === word.length - 1) {
      return true;
    }

    let found = false;

    for (let j = 0; j < dx.length; j++) {
      const nx = cx + dx[j];
      const ny = cy + dy[j];

      if (nx >= 0 && nx < w && ny >= 0 && ny < h && !checked[ny][nx]) {
        if (board[ny][nx] === word[i + 1]) {
          checked[ny][nx] = true;

          if (findWord([ny, nx], i + 1, word)) {
            found = true;
          }

          checked[ny][nx] = false;
        }
      }
    }

    return found;
  };

  const answer = [];

  for (const word of words) {
    let found = false;

    for (let i = 0; i < h; i++) {
      if (found) {
        break;
      }

      for (let j = 0; j < w; j++) {
        if (found) {
          break;
        }

        if (board[i][j] === word[0]) {
          checked[i][j] = true;

          if (findWord([i, j], 0, word)) {
            answer.push(word);
            found = true;
          }

          checked[i][j] = false;
        }
      }
    }
  }

  return answer;
};
