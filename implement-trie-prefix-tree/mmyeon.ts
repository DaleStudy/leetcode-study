class TrieNode {
  children: Map<string, TrieNode>;
  isEndOfWord: boolean;

  constructor() {
    // 키 : 문자, 값 : 다음 문자 노드
    this.children = new Map();
    this.isEndOfWord = false;
  }
}

/**
 * @link https://leetcode.com/problems/implement-trie-prefix-tree/description/
 *
 * 접근 방법 :
 *  - root 노드에서 시작해서 각 문자열을 children노드에 저장한다.
 *  - 문자열의 마지막 문자일 때 끝을 나타내기 위해서 isEndOfWord값을 true로 변경해준다.
 *  - insert : 각 문자열 순회하면서, 문자에 대한 children노드가 없으면 생성해서 문자와 다음 노드를 연결해준다.
 *
 * 시간복잡도 : O(n)
 *  - 문자 길이 n 만큼 문자 삽입함
 *
 * 공간복잡도 : O(n)
 *  - 최대 문자열 길이만큼 노드 추가됨
 */

class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    let currentNode = this.root;

    for (const letter of word) {
      // 현재 문자가 자식 노드에 있으면 이동
      // 없으면 새 노드 생성해서 추가하기
      if (!currentNode.children.has(letter)) {
        currentNode.children.set(letter, new TrieNode());
      }
      // 자식 노드로 이동
      currentNode = currentNode.children.get(letter) as TrieNode;
    }
    currentNode.isEndOfWord = true;
  }

  search(word: string): boolean {
    let currentNode = this.root;

    for (const letter of word) {
      if (!currentNode.children.has(letter)) return false;
      currentNode = currentNode.children.get(letter) as TrieNode;
    }
    return currentNode.isEndOfWord;
  }

  startsWith(prefix: string): boolean {
    let currentNode = this.root;

    for (const letter of prefix) {
      if (!currentNode.children.has(letter)) return false;
      currentNode = currentNode.children.get(letter) as TrieNode;
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
