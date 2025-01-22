var WordDictionary = function() {
  this.children = {};
  this.isEnd = false;
};
/**
* 시간 복잡도: word의 길이만큼 순회하므로, O(n)
* 공간 복잡도: 최대 word의 길이만큼 추가 노드를 생성하므로, O(n)
*/
/** 
* @param {string} word
* @return {void}
*/
WordDictionary.prototype.addWord = function(word) {
  let children = this.children;
  for(let w of word) {
      if(!children[w]) {
          children[w] = {};
          children[w].isEnd = false;
      }
      children = children[w];
  }
  children.isEnd = true;
};
/**
* 시간 복잡도: 
*   최악의 경우 각 노드의 자식 노드는 모든 알파벳의 갯수인 26이 되고,
*   재귀 호출 스택의 깊이는 word.length에 비례하므로,
*   word의 길이가 n이면, 시간 복잡도는 O(26^n)
* 공간 복잡도: 
*   호출 스택 깊이는 n이므로, 공간 복잡도는 O(n)
*/
/** 
* @param {string} word
* @return {boolean}
*/
WordDictionary.prototype.search = function(word) {
  let children = this.children;
  return this.dfs(0, word, children)
};

WordDictionary.prototype.dfs = function(i, word, children) {
  if(i === word.length) {
      return children.isEnd;
  }
  if(word[i] === '.') {
      for(const c in children) {
          if(c === 'isEnd') continue;
          if(this.dfs(i+1, word, children[c])) {
              return true;
          }
      }
      return false;
  } else {
      if(!children[word[i]]) {
          return false;
      }
      return this.dfs(i+1, word, children[word[i]]);
  }
}

/** 
* Your WordDictionary object will be instantiated and called as such:
* var obj = new WordDictionary()
* obj.addWord(word)
* var param_2 = obj.search(word)
*/
