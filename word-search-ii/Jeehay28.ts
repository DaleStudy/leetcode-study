// TC: O(K × L + M × N × 4^L)
// SC: O(K × L + L)
// K: num of words
// L: length of the longest word

function findWords(board: string[][], words: string[]): string[] {
  const result: string[] = [];
  const root: TrieNode = buildTrie(words);
  const rows = board.length;
  const cols = board[0].length;

  function backtrack(row: number, col: number, node: TrieNode) {
    const char = board[row][col];
    const nextNode = node[char] as TrieNode;

    if (!nextNode) return;

    const word = nextNode["$"];
    if (typeof word === "string") {
      result.push(word);
      delete nextNode["$"]; // avoid duplicate
    }

    board[row][col] = ""; // mark as visited

    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    for (const [dx, dy] of directions) {
      const newRow = row + dx;
      const newCol = col + dy;

      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        board[newRow][newCol] !== "$"
      ) {
        backtrack(newRow, newCol, nextNode);
      }
    }

    board[row][col] = char;
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      backtrack(r, c, root);
    }
  }

  return result;
}

// Trie
// {
//   "e": {
//     "a": {
//       "t": {
//         "#": "eat"
//       }
//     }
//   }
// }

type TrieNode = {
  [key: string]: TrieNode | string;
};

function buildTrie(words: string[]): TrieNode {
  const root: TrieNode = {};
  for (const word of words) {
    let node = root;
    for (const char of word) {
      if (!node[char]) node[char] = {};
      node = node[char] as TrieNode;
    }
    node["$"] = word; // end of word
  }
  return root;
}
