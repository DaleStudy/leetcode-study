function Node() {
  this.value = null;
  this.wordGraph = new Map();
}

var Trie = function () {
  this.wordGraph = new Map();
};

/**
 * TC: O(W)
 * SC: O(W)
 * W: word.length
 */

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
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
 * TC: O(W)
 * SC: O(1)
 * W: word.length
 */

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  let pointer = this;
  for (const w of word) {
    if (!pointer.wordGraph.has(w)) {
      return false;
    } else {
      pointer = pointer.wordGraph.get(w);
    }
  }
  return pointer.value === word;
};

/**
 * TC: O(P)
 * SC: O(1)
 * P:prefix.length
 */

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  let pointer = this;
  for (const p of prefix) {
    if (!pointer.wordGraph.has(p)) {
      return false;
    } else {
      pointer = pointer.wordGraph.get(p);
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
