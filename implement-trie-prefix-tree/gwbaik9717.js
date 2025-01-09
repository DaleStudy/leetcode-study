var Node = function () {
  this.children = new Map();
  this.isEnd = false;
};

var Trie = function () {
  this.head = new Node();
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let current = this.head;

  for (const chr of word) {
    if (!current.children.has(chr)) {
      current.children.set(chr, new Node());
    }

    current = current.children.get(chr);
  }

  current.isEnd = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  let current = this.head;

  for (const chr of word) {
    if (!current.children.has(chr)) {
      return false;
    }

    current = current.children.get(chr);
  }

  return current.isEnd;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  let current = this.head;

  for (const chr of prefix) {
    if (!current.children.has(chr)) {
      return false;
    }

    current = current.children.get(chr);
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