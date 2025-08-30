var WordDictionary = function () {
  this.trie = {}; // Trie 루트 노드
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let current = this.trie;

  // 각 문자마다 노드 생성
  for (let i = 0; i < word.length; i++) {
    const char = word[i];
    if (!current[char]) {
      current[char] = {};
    }
    current = current[char];
  }

  // 단어의 끝 표시
  current.isEnd = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  return dfs(word, 0, this.trie);
};

/**
 * @param {string} word - 검색할 단어
 * @param {number} index - 현재 검사 중인 문자 인덱스
 * @param {object} node - 현재 Trie 노드
 * @return {boolean}
 */
function dfs(word, index, node) {
  // 단어 끝에 도달했으면 isEnd 확인
  if (index === word.length) {
    return !!node.isEnd;
  }

  const char = word[index];

  if (char === '.') {
    // '.'인 경우: 모든 자식 노드를 탐색
    for (let key in node) {
      if (key !== 'isEnd') {
        // isEnd 속성은 제외
        if (dfs(word, index + 1, node[key])) {
          return true;
        }
      }
    }
    return false;
  } else {
    // 일반 문자인 경우: 해당 문자의 노드로 이동
    if (!node[char]) {
      return false;
    }
    return dfs(word, index + 1, node[char]);
  }
}
