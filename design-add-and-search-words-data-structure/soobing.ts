/**
 *
 * 문제 설명
 * - 문자열 추가/검색에 효율적인 데이터 구조 설계
 *
 * 아이디어
 * 1) 배열에 추가, 순차적으로 검색(.의 경우 정규식 사용)
 * - Time Limit Exceeded (TLE) 발생
 *
 * 2) Trie 구조로 저장, 검색은 dfs
 * - 문자열 검색어 최적화 = Trie
 *
 */

class TrieNode {
  children: Map<string, TrieNode> = new Map();
  isEnd: boolean = false;
}

class WordDictionary {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  addWord(word: string): void {
    let node = this.root;
    for (let char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char)!;
    }
    node.isEnd = true;
  }

  search(word: string): boolean {
    const dfs = (node: TrieNode, i: number) => {
      if (i === word.length) return node.isEnd;

      const char = word[i];

      if (char === ".") {
        for (let child of node.children.values()) {
          if (dfs(child, i + 1)) return true;
        }
        return false;
      } else {
        const next = node.children.get(char);
        return next ? dfs(next, i + 1) : false;
      }
    };

    return dfs(this.root, 0);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
