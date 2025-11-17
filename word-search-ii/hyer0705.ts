// 84ms
class TrieNode {
  children: Map<string, TrieNode>;
  isEndOf: boolean;
  word: string | null;

  constructor() {
    this.children = new Map();
    this.word = null;
  }
}
class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string) {
    let current = this.root;

    for (const char of word) {
      if (!current.children.has(char)) {
        current.children.set(char, new TrieNode());
      }
      current = current.children.get(char);
    }

    current.word = word;
  }
}

function findWords(board: string[][], words: string[]): string[] {
  const m = board.length;
  const n = board[0].length;

  const dictionary = new Trie();
  for (const word of words) {
    dictionary.insert(word);
  }

  const results: string[] = [];

  const dfs = (row: number, col: number, trieNode: TrieNode) => {
    if (trieNode.word !== null) {
      results.push(trieNode.word);
      trieNode.word = null;
    }

    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];

    for (const [dr, dc] of directions) {
      const [nr, nc] = [row + dr, col + dc];

      if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
        if (trieNode.children.has(board[nr][nc])) {
          const char = board[nr][nc];
          const childNode = trieNode.children.get(char);

          if (board[nr][nc] !== "#") {
            board[nr][nc] = "#";
            dfs(nr, nc, trieNode.children.get(char));
            board[nr][nc] = char;
          }

          if (childNode.children.size === 0 && childNode.word === null) {
            trieNode.children.delete(char);
          }
        }
      }
    }
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const firstChar = board[i][j];
      if (dictionary.root.children.has(firstChar)) {
        board[i][j] = "#";
        dfs(i, j, dictionary.root.children.get(firstChar));
        board[i][j] = firstChar;
      }
    }
  }

  return results;
}

// 2312ms
class TrieNode {
  children: Map<string, TrieNode>;
  word: string | null;

  constructor() {
    this.children = new Map();
    this.word = null;
  }
}
class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string) {
    let current = this.root;

    for (const char of word) {
      if (!current.children.has(char)) {
        current.children.set(char, new TrieNode());
      }
      current = current.children.get(char)!;
    }

    current.word = word;
  }
}

function findWords(board: string[][], words: string[]): string[] {
  const m = board.length;
  const n = board[0].length;

  const dictionary = new Trie();
  for (const word of words) {
    dictionary.insert(word);
  }

  const results: string[] = [];

  const dfs = (row: number, col: number, trieNode: TrieNode, path: string) => {
    if (trieNode.word === path) {
      results.push(path);
      trieNode.word = null;
    }

    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];

    for (const [dr, dc] of directions) {
      const [nr, nc] = [row + dr, col + dc];

      if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
        if (trieNode.children.has(board[nr][nc])) {
          if (!isVisited.has(`${nr},${nc}`)) {
            isVisited.add(`${nr},${nc}`);
            dfs(nr, nc, trieNode.children.get(board[nr][nc])!, path + board[nr][nc]);
            isVisited.delete(`${nr},${nc}`);
          }
        }
      }
    }
  };

  const isVisited = new Set<string>(); // 'r,c'
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const firstChar = board[i][j];
      if (dictionary.root.children.has(firstChar)) {
        isVisited.add(`${i},${j}`);
        dfs(i, j, dictionary.root.children.get(firstChar)!, firstChar);
        isVisited.delete(`${i},${j}`);
      }
    }
  }

  return results;
}
