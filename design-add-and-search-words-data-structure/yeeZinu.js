// node 함수선언
function Node() {
  this.child = {};
  this.end = false;
}

// 최상단의 루트를 노드로 초기화
var WordDictionary = function () {
  this.root = new Node();
};

/** 
* @param {string} word
* @return {void}
*/
WordDictionary.prototype.addWord = function (word) {
  // 현재위치를 최상단으로 초기화
  let current = this.root;

  // 문자를 받고 단어하나씩 노드에 저장
  for (const char of word) {
    if (!current.child[char]) {
      current.child[char] = new Node();
    }
    current = current.child[char];
  }

  // 반복이 끝났으면 true;
  current.end = true;

};

/** 
* @param {string} word
* @return {boolean}
*/
WordDictionary.prototype.search = function (word) {

  // i 를 받아 단어 만큼 재귀하는 함수
  const searchHelper = (current, i) => {
    // i와 단어의 길이가 같으면 종료
    if (i === word.length) return current.end;

    // 단어 = 찾을 문자의 i번째 단어
    const char = word[i];

    // 만약 문자가 . 라면
    if (char === '.') {
      // 해당 현재 것들의 키를 가지고 반복
      for (const char of Object.keys(current.child)) {
        const children = current.child[char];
        // end를 true로 하고 i+1로 재귀
        if (searchHelper(children, i + 1)) return true;
      }
      return false;
    }
    else {
      // 현재 자식에 해당 문자가 없으면 false
      if (!(char in current.child)) return false;
      // 아니면 한번 더 재귀
      return searchHelper(current.child[char], i + 1);
    }
  }
  // 결과 리턴
  return searchHelper(this.root, 0);
};

/** 
* Your WordDictionary object will be instantiated and called as such:
* var obj = new WordDictionary()
* obj.addWord(word)
* var param_2 = obj.search(word)
*/
