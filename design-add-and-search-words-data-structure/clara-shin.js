/**
 * 단어를 저장하고 검색할 수 있는 자료구조 만들기
 *
 * 트라이(Trie) 자료구조: 문자열 집합을 표현하는 트리 기반 자료구조, (문자열 검색에 효율적)
    - 각 노드는 문자 하나를 나타냄
    - 루트에서 특정 노드까지의 경로는 하나의 문자열을 나타냄
    - 각 노드는 자식 노드들을 가리키는 링크(보통 해시맵)를 가짐
    - 단어의 끝을 표시하는 플래그가 필요함
 *
 * 대부분의 검색은 와일드카드가 없는 경우일 테니까, 이것만 처리하는 별도 메서드로 뽑음(와일드카드 분기처리)
 * 
 * 시간복잡도: O(m) (m: 단어의 길이)
 * 공간복잡도: O(n) (n: 단어의 개수)
 */

var WordDictionary = function () {
  // 트라이 노드 클래스 정의
  this.TrieNode = function () {
    this.children = {}; // 자식 노드들을 저장하는 해시맵
    this.isEnd = false; // 단어의 끝을 표시하는 플래그
  };

  this.root = new this.TrieNode(); // 루트 노드 생성
};

/**
 * 단어를 트라이에 추가
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let node = this.root;

  // 단어의 각 문자를 순회하며 트라이에 추가
  for (let i = 0; i < word.length; i++) {
    const char = word[i];

    // 현재 문자에 해당하는 자식 노드가 없으면 생성
    if (!node.children[char]) {
      node.children[char] = new this.TrieNode();
    }

    // 다음 레벨로 이동
    node = node.children[char];
  }

  // 단어의 끝 표시
  node.isEnd = true;
};

/**
 * 트라이에서 단어 검색 (와일드카드 '.' 지원)
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  // 와일드카드가 없는 경우
  if (!word.includes('.')) {
    return this.searchExact(word);
  }

  return this.searchWithWildcard(word, 0, this.root);
};

/**
 * 와일드카드 없이 정확한 단어 검색
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.searchExact = function (word) {
  let node = this.root;

  for (let i = 0; i < word.length; i++) {
    const char = word[i];

    // 해당 문자의 자식 노드가 없으면 false
    if (!node.children[char]) {
      return false;
    }

    node = node.children[char];
  }

  // 단어의 끝에 도달했을 때 isEnd 플래그 확인
  return node.isEnd;
};

/**
 * 와일드카드를 포함한 단어 검색 (재귀적)
 * @param {string} word - 검색할 단어
 * @param {number} index - 현재 검색중인 문자 인덱스
 * @param {object} node - 현재 검색중인 노드
 * @return {boolean}
 */
WordDictionary.prototype.searchWithWildcard = function (word, index, node) {
  // 단어의 모든 문자를 검사했으면
  if (index === word.length) {
    return node.isEnd;
  }

  const char = word[index];

  // 와일드카드('.')인 경우
  if (char === '.') {
    // 현재 노드의 모든 자식에 대해 재귀적으로 검색
    for (const key in node.children) {
      if (this.searchWithWildcard(word, index + 1, node.children[key])) {
        return true;
      }
    }
    return false;
  }
  // 일반 문자인 경우
  else {
    // 해당 문자에 대한 자식 노드가 없으면 false
    if (!node.children[char]) {
      return false;
    }

    // 다음 문자 검색
    return this.searchWithWildcard(word, index + 1, node.children[char]);
  }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
