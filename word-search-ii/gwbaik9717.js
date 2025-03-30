// k: length of word, h: height of board, w: width of board
// Time complexity: O(4^k * h * w)
// Space complexity: O(4^k)

class Node {
  constructor(value = "") {
    this.value = value;
    this.children = new Map();
    this.isEnd = false;
  }
}
class Trie {
  constructor() {
    this.head = new Node();
  }

  add(str) {
    let current = this.head;

    for (const chr of str) {
      if (!current.children.has(chr)) {
        current.children.set(chr, new Node(current.value + chr));
      }

      current = current.children.get(chr);
    }

    current.isEnd = true;
  }
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
  const answer = new Set();

  const h = board.length;
  const w = board[0].length;

  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];
  const checked = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => false)
  );

  const dfs = (current, children) => {
    const [cy, cx] = current;

    if (!children.has(board[cy][cx])) {
      return;
    }

    if (children.get(board[cy][cx]).isEnd) {
      answer.add(children.get(board[cy][cx]).value);
    }

    for (let j = 0; j < dx.length; j++) {
      const nx = cx + dx[j];
      const ny = cy + dy[j];

      if (nx >= 0 && nx < w && ny >= 0 && ny < h && !checked[ny][nx]) {
        checked[ny][nx] = true;
        dfs([ny, nx], children.get(board[cy][cx]).children);
        checked[ny][nx] = false;
      }
    }
  };

  const trie = new Trie();

  for (const word of words) {
    trie.add(word);
  }

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      checked[i][j] = true;
      dfs([i, j], trie.head.children);
      checked[i][j] = false;
    }
  }

  return [...answer];
};
