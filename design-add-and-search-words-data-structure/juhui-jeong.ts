/*
시간복잡도: O(L)
공간복잡도: O(L)
Trie는 검색을 빠르게 해주지만,
. 와일드카드는 DFS 분기를 유발해 최악의 경우 시간 복잡도가 커질 수 있다.

DFS가 필요한 검색 문제에 대한 공부 필요.
*/
class TrieNode {
  children: Map<string, TrieNode>;
  isEnd: boolean;

  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class WordDictionary {
  private root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  addWord(word: string): void {
    let node = this.root;

    for (const ch of word) {
      if (!node.children.has(ch)) {
        node.children.set(ch, new TrieNode());
      }
      node = node.children.get(ch)!;
    }
    node.isEnd = true;
  }

  search(word: string): boolean {
    const dfs = (index: number, node: TrieNode): boolean => {
      if (index === word.length) {
        return node.isEnd;
      }

      const ch = word[index];

      if (ch === '.') {
        for (const child of node.children.values()) {
          if (dfs(index + 1, child)) return true;
        }
        return false;
      }

      const next = node.children.get(ch);
      if (!next) return false;

      return dfs(index + 1, next);
    };

    return dfs(0, this.root);
  }
}
