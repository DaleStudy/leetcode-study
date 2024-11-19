/**
 * https://leetcode.com/problems/word-search-ii
 * T.C. O(W * L + M * N * 4^L) W: number of words, L: mean length of words, M: rows, N: cols
 * S.C. O(W * L)
 */
function findWords(board: string[][], words: string[]): string[] {
  const root = new TrieNode();
  for (const word of words) {
    let node = root;
    for (const char of word) {
      if (!node.children[char]) {
        node.children[char] = new TrieNode();
      }
      node = node.children[char];
    }
    node.word = word;
    node.isEnd = true;
  }

  const result = new Set<string>();
  const rows = board.length;
  const cols = board[0].length;

  function dfs(row: number, col: number, node: TrieNode): void {
    if (row < 0 || row >= rows) return;
    if (col < 0 || col >= cols) return;
    if (!board[row][col]) return;
    if (!node.children[board[row][col]]) return;

    const char = board[row][col];
    const currNode = node.children[char];

    if (currNode.isEnd) {
      result.add(currNode.word);
    }

    board[row][col] = '#';

    dfs(row + 1, col, currNode);
    dfs(row - 1, col, currNode);
    dfs(row, col + 1, currNode);
    dfs(row, col - 1, currNode);

    board[row][col] = char;
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      dfs(i, j, root);
    }
  }

  return Array.from(result);
}

class TrieNode {
  constructor(
    public children: Record<string, TrieNode> = {},
    public word: string = '',
    public isEnd: boolean = false
  ) {}
}
