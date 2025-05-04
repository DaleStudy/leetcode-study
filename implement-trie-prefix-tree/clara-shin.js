// TrieNode 클래스 정의: 트라이의 각 노드를 표현
var TrieNode = function () {
  this.children = new Map(); // 자식 노드를 Map으로 저장
  this.isEnd = false; // 단어의 끝을 표시하는 플래그
};

// Trie 클래스 정의: 트라이 자료구조를 표현
var Trie = function () {
  this.root = new TrieNode(); // 루트 노드
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let node = this.root; // 현재 노드를 루트로 초기화

  for (let i = 0; i < word.length; i++) {
    const char = word[i]; // 현재 문자

    // 현재 문자에 대한 자식 노드가 없으면 새로 생성
    if (!node.children.has(char)) {
      node.children.set(char, new TrieNode());
    }

    // 다음 자식 노드로 이동
    node = node.children.get(char);
  }
  node.isEnd = true; // 단어의 끝을 표시
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  const node = this._searchPrefix(word); // 주어진 단어의 노드를 찾음
  return node !== null && node.isEnd === true; // 경로가 존재하고, 마지막 노드가 단어의 끝인지 확인
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  return this._searchPrefix(prefix) !== null; // 경로가 존재하는지만 확인
};

/**
 * 헬퍼 메서드: 주어진 접두사에 대한 경로를 찾는 메서드
 * @param {string} str
 * @return {TrieNode|null} 경로의 마지막 노드 또는 null
 * @private
 */
Trie.prototype._searchPrefix = function (str) {
  let node = this.root; // 현재 노드를 루트로 초기화

  // 주어진 문자열의 각 문자에 대해 노드 탐색
  for (let i = 0; i < str.length; i++) {
    const char = str[i]; // 현재 문자

    // 현재 문자에 대한 자식 노드가 없으면 null 리턴
    if (!node.children.has(char)) {
      return null;
    }

    // 다음 자식 노드로 이동
    node = node.children.get(char);
  }
  return node; // 경로의 마지막 노드 반환
};
/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
