// trieNode 클래스 선언
// child = {}, end = false 로 초기화
class TrieNode {
  constructor(child = {}, end = false) {
      this.child = child;
      this.end = end;
  }
}

// Trie함수의 root는 TrieNode의 객체
var Trie = function() {
  this.root = new TrieNode();
};

/** 
* @param {string} word
* @return {void}
*/
// 단어 삽입
Trie.prototype.insert = function(word) {
  // 현재 = 최상단으로 초기화
  let current = this.root;
  
  // 단어를 반복하면서 없으면 TrieNode에 추가
  for (const char of word) {
      if (!current.child[char]) {
          current.child[char] = new TrieNode();
      } 
      current = current.child[char];
  }

  // 반복이 끝나면 end true
  current.end = true;
};

/** 
* @param {string} word
* @return {boolean}
*/
// 단어 탐색
Trie.prototype.search = function(word) {
  // 현재위치 = 최상단으로
  let current = this.root;

  // 반복하면서 단어찾기
  for(const char of word) {
      if(current.child[char]) {
          current = current.child[char];
      }
      else {
          return false;
      }
  }
  return current.end;
  
};

/** 
* @param {string} prefix
* @return {boolean}
*/
Trie.prototype.startsWith = function(prefix) {
  let current = this.root;
  for (const char of prefix) {
      if (current.child[char]) {
          current = current.child[char];
      }
      else {
          return false;
      }
  }

  return true;
};

/** 
* Your Trie object will be instantiated and called as such:
* var obj = new Trie()
* obj.insert(word)
* var param_2 = obj.search(word)
* var param_3 = obj.startsWith(prefix)
*/
