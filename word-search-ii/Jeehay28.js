// const words = ["oath", "pea", "eat", "rain"];
// const trie = buildTrie(words);

// Trie in JavaScript Object Notation:
// {
//   "o": { "a": { "t": { "h": { "word": "oath" } } } },
//   "p": { "e": { "a": { "word": "pea" } } },
//   "e": { "a": { "t": { "word": "eat" } } },
//   "r": { "a": { "i": { "n": { "word": "rain" } } } }
// }

class TrieNode {
  constructor() {
    this.children = {}; // Stores child nodes (next characters)
    this.word = null; // Stores the word when a full word is formed
  }
}

const buildTrie = (words) => {
  let root = new TrieNode(); // Create the root node

  for (const word of words) {
    // Iterate over each word
    let node = root;

    for (const char of word) {
      // Iterate over each character in the word
      if (!node.children[char]) {
        node.children[char] = new TrieNode(); // Create node if missing
      }
      node = node.children[char]; // Move to the next node
    }

    node.word = word; // Store word at the end node
  }

  return root;
};

// ✅ Time Complexity: O(N * L + M * 4^L)
// ✅ Space Complexity: O(N * L + M)

// N represents the number of words in the words array.
// L represents the maximum length of a word in the words array.
// M represents the total number of cells on the board, which is the product of the number of rows and columns: M = rows × cols

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
  const root = buildTrie(words);
  const result = new Set(); // To store found words
  const rows = board.length,
    cols = board[0].length;

  const dfs = (node, r, c) => {
    if (
      r < 0 ||
      c < 0 ||
      r >= rows ||
      c >= cols ||
      !node.children[board[r][c]]
    ) {
      return;
    }

    const char = board[r][c];
    node = node.children[char]; // Move to the next Trie node

    if (node.word) {
      // If a word is found at this node
      result.add(node.word); // Add it to the result set
      node.word = null; // Avoid duplicate results
    }

    board[r][c] = "#"; // Temporarily mark visited cell

    // Explore all 4 directions
    dfs(node, r + 1, c);
    dfs(node, r - 1, c);
    dfs(node, r, c + 1);
    dfs(node, r, c - 1);

    board[r][c] = char; // Restore the original character

    // 🔥 Remove node if it has no children (prune Trie)
    if (Object.keys(node.children).length === 0) {
      delete node.children[char];
    }
  };

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (root.children[board[r][c]]) {
        dfs(root, r, c);
      }
    }
  }

  return Array.from(result);
};

