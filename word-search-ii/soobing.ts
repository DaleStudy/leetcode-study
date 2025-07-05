/**
 * 문제 설명
 * - 2차원 배열에서 주어진 단어들을 찾는 문제
 *
 * 아이디어
 * 1) Trie 자료구조 + DFS & Backtracking (👀어려웠음..다시 풀어보기)
 *   - 주어진 단어들을 Trie 자료구조로 변환
 *   - 2차원 배열을 순회하면서 Trie 자료구조를 사용하여 단어를 찾음
 *   - 찾은 단어는 배열에 추가
 */
class TrieNode {
  private nodes = new Map<string, TrieNode>();
  word: string | null = null;

  add(word: string) {
    let currentNode = this as TrieNode;
    for (const char of word) {
      if (!currentNode.nodes.has(char)) {
        currentNode.nodes.set(char, new TrieNode());
      }
      currentNode = currentNode.nodes.get(char)!;
    }
    currentNode.word = word;
  }

  getNode(char: string) {
    return this.nodes.get(char);
  }

  hasChar(char: string) {
    return this.nodes.has(char);
  }
}

function search(
  m: number,
  n: number,
  board: string[][],
  node: TrieNode,
  result: string[]
) {
  const M = board.length;
  const N = board[0].length;
  if (m < 0 || m >= M || n < 0 || n >= N) return;

  const currentChar = board[m][n];
  if (currentChar === "#" || !node.hasChar(currentChar)) return;

  node = node.getNode(currentChar)!;

  if (node.word) {
    result.push(node.word);
    node.word = null;
  }

  board[m][n] = "#";

  search(m + 1, n, board, node, result);
  search(m - 1, n, board, node, result);
  search(m, n + 1, board, node, result);
  search(m, n - 1, board, node, result);

  board[m][n] = currentChar;
}

function findWords(board: string[][], words: string[]): string[] {
  const root = new TrieNode();
  for (const word of words) {
    root.add(word);
  }

  const result: string[] = [];
  const M = board.length;
  const N = board[0].length;

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      search(i, j, board, root, result);
    }
  }

  return result;
}
