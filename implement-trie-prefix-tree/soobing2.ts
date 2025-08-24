/**
 * 문제 유형
 * - Trie 구현 (문자열 검색)
 *
 * 문제 설명
 * - 문자열 검색/추천/자동완성에서 자주 사용하는 자료구조 Trie 구현
 *
 * 아이디어
 * 1) 문자열의 각 문자를 TrieNode 클래스의 인스턴스로 표현s
 *
 */
class TrieNode {
  children: Map<string, TrieNode>;
  isEnd: boolean;

  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Trie {
  root: TrieNode;
  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char)!;
    }
    node.isEnd = true;
  }

  // isEnd 까지 확인이 필요
  search(word: string): boolean {
    const node = this._findNode(word);
    return node !== null && node.isEnd;
  }

  // isEnd까지 확인 필요 없고 존재 여부만 확인 필요
  startsWith(prefix: string): boolean {
    return this._findNode(prefix) !== null;
  }

  private _findNode(word: string): TrieNode | null {
    let node = this.root;
    for (const char of word) {
      if (!node.children.get(char)) return null;
      node = node.children.get(char)!;
    }

    return node;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
