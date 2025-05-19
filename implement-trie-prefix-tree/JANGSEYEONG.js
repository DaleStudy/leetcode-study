/**
 * Trie(트라이) 데이터 구조 구현
 *
 * 원리: 트라이는 문자열을 효율적으로 저장하고 검색하기 위한 트리 구조
 * 각 노드는 한 문자를 나타내며, 루트에서 특정 노드까지의 경로가 하나의 문자열이 된다
 * 공통 접두사를 공유하여 메모리를 절약하고, 접두사 검색을 O(k) 시간에 수행할 수 있음
 */
var Trie = function () {
  this.root = {}; // 루트 노드
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let node = this.root;

  for (let char of word) {
    if (!node[char]) {
      // 처음 들어오는 단어일 경우, 새 트리구조 생성
      node[char] = {};
    }
    // 현재 단어 위치로 이동
    node = node[char];
  }
  node.isEnd = true; // 단어 끝 표시
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  let node = this.traverse(word);
  return node !== null && node.isEnd === true;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  return this.traverse(prefix) !== null;
};

/**
 * 주어진 문자열을 따라 트라이를 탐색하는 함수
 * @param {string} str - 트라이에서 탐색할 문자열
 * @return {object|null} - 문자열 경로의 마지막 노드 또는 경로가 없으면 null
 */
Trie.prototype.traverse = function (str) {
  let node = this.root;

  // 문자열의 각 문자를 하나씩 순회
  for (let char of str) {
    // 현재 문자에 대한 경로가 없으면 탐색 실패
    if (!node[char]) {
      return null;
    }
    // 해당 문자의 노드로 이동하여 탐색 계속
    node = node[char];
  }
  return node;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
