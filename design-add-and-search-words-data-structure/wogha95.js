function Node() {
  // 단어의 끝을 의미 + 무슨 단어인지 저장
  this.value = null;
  // 단어의 다음 문자로 연결되어 있는 노드맵
  this.wordGraph = new Map();
}

var WordDictionary = function () {
  this.wordGraph = new Map();
};

/**
 * TC: O(N)
 * SC: O(N)
 */

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let pointer = this;
  for (const w of word) {
    if (!pointer.wordGraph.has(w)) {
      pointer.wordGraph.set(w, new Node());
    }
    pointer = pointer.wordGraph.get(w);
  }
  pointer.value = word;
};

/**
 * TC: O(D^W)
 * SC: O(D * W)
 *
 * W: word.length, D: count of Dictionary.wordGraph keys
 *
 * 풀이: Trie 자료구조 + bfs탐색
 */

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  const queue = [{ pointer: this, index: 0 }];

  // 1. BFS 탐색 방법 이용
  while (queue.length > 0) {
    const { pointer, index } = queue.shift();

    // 2. 찾고자하는 단어의 끝에 도달했으면 해당 단어가 있는지 확인한다.
    if (index === word.length) {
      if (pointer.value !== null) {
        return true;
      }
      continue;
    }

    if (word[index] === ".") {
      // 3. 찾고자하는 단어의 문자가 '.'인 경우, 현재 graph에서 이어진 문자를 모두 탐색(queue에 추가)
      for (const [key, node] of pointer.wordGraph) {
        queue.push({ pointer: node, index: index + 1 });
      }
    } else if (pointer.wordGraph.has(word[index])) {
      // 4. 찾고자하는 단어의 문자가 graph에 있는 경우 탐색(queue에 추가)
      queue.push({
        pointer: pointer.wordGraph.get(word[index]),
        index: index + 1,
      });
    }
  }

  // 5. 더이상 탐색할 것이 없다면 해당 단어 없음으로 판단
  return false;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
