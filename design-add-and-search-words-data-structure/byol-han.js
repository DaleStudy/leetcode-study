// 각 문자 노드를 나타내는 TrieNode 클래스
class TrieNode {
  constructor() {
    this.children = {}; // 자식 노드들을 저장하는 객체 (예: { a: TrieNode, b: TrieNode, ... })
    this.isEndOfWord = false; // 단어가 이 노드에서 끝나는지 여부
  }
}

class WordDictionary {
  constructor() {
    this.root = new TrieNode(); // 루트 노드 생성 (모든 단어의 시작점)
  }

  /**
   * 단어를 Trie에 추가
   * @param {string} word
   */
  addWord(word) {
    let node = this.root;
    for (let char of word) {
      // 현재 문자가 자식 노드에 없으면 새 노드 생성
      if (!node.children[char]) {
        node.children[char] = new TrieNode();
      }
      // 다음 문자로 이동
      node = node.children[char];
    }
    // 단어가 끝나는 지점 표시
    node.isEndOfWord = true;
  }

  /**
   * 단어 검색 (.은 와일드카드로 어떤 문자든 대체 가능)
   * @param {string} word
   * @returns {boolean}
   */
  search(word) {
    /**
     * DFS 방식으로 검색을 수행 (백트래킹 포함)
     * @param {TrieNode} node - 현재 노드
     * @param {number} i - 현재 탐색 중인 문자 인덱스
     */
    const dfs = (node, i) => {
      // 단어 끝에 도달하면 isEndOfWord 여부 반환
      if (i === word.length) {
        return node.isEndOfWord;
      }

      const char = word[i];

      // 현재 문자가 '.'일 경우 모든 자식 노드 탐색
      if (char === ".") {
        for (let child of Object.values(node.children)) {
          // 하나라도 성공하면 true 반환
          if (dfs(child, i + 1)) return true;
        }
        // 모든 자식 노드가 실패하면 false 반환
        return false;
      } else {
        // 해당 문자로 연결된 자식 노드가 없으면 false
        if (!node.children[char]) return false;
        // 다음 문자로 재귀 호출
        return dfs(node.children[char], i + 1);
      }
    };

    // 루트 노드부터 검색 시작
    return dfs(this.root, 0);
  }
}
