var Trie = function() {
  this.root = {};
};

/** 
 * @param {string} word
 * @return {void}
 * 
 * complexity
 * time: O(n)
 * space: O(n)
 */
Trie.prototype.insert = function(word) {
  let cur = this.root;
  for (let x of word) {
      if (!cur[x]) cur[x] = {};
      cur = cur[x];
  }
  cur.end = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */
Trie.prototype.search = function(word) {
  let cur = this.find(word);
  return cur !== null && cur.end === true;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */
Trie.prototype.startsWith = function(prefix) {
  return this.find(prefix) !== null;
};

/**
 * @param {string} str
 * @return {object}
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */
Trie.prototype.find = function(str) {
  let cur = this.root;
  for (let x of str) {
      if (!cur[x]) return null;
      cur = cur[x];
  }
  return cur;
};

