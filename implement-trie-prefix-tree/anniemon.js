/**
 * 시간 복잡도: 주어진 문자열의 길이만큼 순회하므로, O(n)
 * 공간 복잡도: 삽입된 모든 문자열의 길이만큼 노드가 만들어지므로, 이를 m이라고 하면 O(m)
 */
var Trie = function() {
  this.isEnd = false;
  this.children = {};
};

/** 
* @param {string} word
* @return {void}
*/
Trie.prototype.insert = function(word) {
  let cur = this.children;
  for(const c of word) {
      if(!cur[c]) {
          cur[c] = { isEnd: false, children: {} };
      }
      cur = cur[c];
  }
  cur.isEnd = true;
};

/** 
* @param {string} word
* @return {boolean}
*/
Trie.prototype.search = function(word) {
  let cur = this.children;
  for(const c of word) {
      if(!cur[c]) {
          return false;
      }
      cur = cur[c]
  }
  return cur.isEnd;
};

/** 
* @param {string} prefix
* @return {boolean}
*/
Trie.prototype.startsWith = function(prefix) {
  let cur = this.children;
  for(const c of prefix) {
      if(!cur[c]){
          return false;
      }
      cur = cur[c];
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
