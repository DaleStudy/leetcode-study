var WordDictionary = function () {
  this.root = {};
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let node = this.root;
  for (const char of word) {
    if (!node[char]) {
      // 현재 문자에 해당하는 노드가 없으면 새로 생성
      node[char] = { isEnd: false };
    }
    node = node[char]; // 다음 노드로 이동
  }
  node.isEnd = true; // 단어 끝 표시
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  function dfs(node, index) {
    // 단어의 끝에 도달했으면 isEnd 값 반환
    if (index === word.length) return node.isEnd;

    const char = word[index];

    if (node[char]) {
      // 현재 문자가 노드에 존재하면 해당 노드로 이동하여 계속 검색
      return dfs(node[char], index + 1);
    }

    if (char === ".") {
      // "."인 경우: 모든 가능한 문자에 대해 검색 시도
      return Object.keys(node)
        .filter((key) => key !== "isEnd")
        .some((key) => dfs(node[key], index + 1)); // 하나라도 true를 반환하면 true
    }

    return false;
  }
  return dfs(this.root, 0);
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
