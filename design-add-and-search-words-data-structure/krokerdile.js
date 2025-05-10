class TrieNode {
    constructor() {
      this.children = {}; // 문자 -> TrieNode 매핑
      this.isEnd = false; // 단어의 끝 표시
    }
  }
  
  class WordDictionary {
    constructor() {
      this.root = new TrieNode();
    }
  
    /**
     * 단어를 트라이에 추가
     * Time Complexity: O(L)  // L = word.length
     * Space Complexity: O(L) // 새로운 노드 최대 L개 추가 가능
     */
    addWord(word) {
      let node = this.root;
      for (const char of word) {
        if (!node.children[char]) {
          node.children[char] = new TrieNode();
        }
        node = node.children[char];
      }
      node.isEnd = true;
    }
  
    /**
     * 단어 또는 패턴 검색
     * Time Complexity: O(26^D * L) // D = '.' 개수 (최대 2), L = word.length
     * Space Complexity: O(L) // DFS 재귀 호출 스택 깊이
     */
    search(word) {
      const dfs = (index, node) => {
        for (let i = index; i < word.length; i++) {
          const char = word[i];
          if (char === '.') {
            for (const child of Object.values(node.children)) {
              if (dfs(i + 1, child)) return true;
            }
            return false;
          } else {
            if (!node.children[char]) return false;
            node = node.children[char];
          }
        }
        return node.isEnd;
      };
  
      return dfs(0, this.root);
    }
  }
